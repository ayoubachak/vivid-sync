from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .service import (
    GoogleRawLoginFlowService,
)
from users.selectors import user_list
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

class PublicApi(APIView):
    authentication_classes = ()
    permission_classes = ()


class GoogleLoginRedirectApi(PublicApi):
    @swagger_auto_schema(operation_description="Redirect to Google for authentication.")
    def get(self, request, *args, **kwargs):
        google_login_flow = GoogleRawLoginFlowService()

        authorization_url, state = google_login_flow.get_authorization_url()

        request.session["google_oauth2_state"] = state 
        request.session.save()
        return redirect(authorization_url)


class GoogleLoginApi(PublicApi):
    class InputSerializer(serializers.Serializer):
        code = serializers.CharField(required=False)
        error = serializers.CharField(required=False)
        state = serializers.CharField(required=False)

    @swagger_auto_schema(
        operation_description="Google OAuth2 callback endpoint.",
        responses={200: "Login successful", 400: "Error"})
    def get(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data

        code = validated_data.get("code")
        error = validated_data.get("error")
        state = validated_data.get("state")

        if error is not None:
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        if code is None or state is None:
            return Response({"error": "Code and state are required."}, status=status.HTTP_400_BAD_REQUEST)

        session_state = request.session.get("google_oauth2_state")
        if session_state is None:
            return Response({"error": "CSRF check failed."}, status=status.HTTP_400_BAD_REQUEST)

        del request.session["google_oauth2_state"]

        if state != session_state:
            return Response({"error": "CSRF check failed."}, status=status.HTTP_400_BAD_REQUEST)

        google_login_flow = GoogleRawLoginFlowService()

        google_tokens = google_login_flow.get_tokens(code=code)
        client_id = google_login_flow._credentials.client_id
        id_token_decoded = google_tokens.decode_id_token(client_id)
        user_info = google_login_flow.get_user_info(google_tokens=google_tokens)
        user_email = id_token_decoded["email"]
        request_user_list = user_list(filters={"email": user_email})
        user = request_user_list.get() if request_user_list else None
        if user is None:
            return Response({"error": f"User with email {user_email} is not found."}, status=status.HTTP_404_NOT_FOUND)
        
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        login(request, user, backend='authentication.backends.JWTAuthenticationBackend')

        result = {
            "id_token_decoded": id_token_decoded,
            "user_info": user_info,
        }

        return redirect('/me/')
        # return Response(result)
from django.urls import path

from .apis import (
    GoogleLoginApi,
    GoogleLoginRedirectApi,
)

from rest_framework.views import APIView
from rest_framework.response import Response
class TestView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        return Response({'msg': 'test'})

app_name = 'google-oauth2'

urlpatterns = [
    path("callback/", GoogleLoginApi.as_view(), name="callback-raw"),
    path("redirect/", GoogleLoginRedirectApi.as_view(), name="redirect-raw"),
    path("test/", TestView.as_view(), name="test-raw"),
]
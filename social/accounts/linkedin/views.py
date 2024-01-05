from django.shortcuts import redirect
from django.conf import settings
import requests
from social.models import SocialMediaPlatform, SocialMediaProfile
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect

class InitiateLinkedInAuth(APIView):
    def get(self, request, *args, **kwargs):
        oauth_url = (
            f"https://www.linkedin.com/oauth/v2/authorization?response_type=code"
            f"&client_id={settings.VIVIDSYNC_LINKEDIN_CLIENT_ID}"
            f"&redirect_uri={settings.VIVIDSYNC_LINKEDIN_REDIRECT_URI}"
            f"&scope=openid%20profile%20w_member_social%20email"
        )
        return HttpResponseRedirect(oauth_url)




class LinkedInCallback(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if not code:
            return redirect('/error/')  # Handle error scenario

        # Exchange code for access token
        response = requests.post('https://www.linkedin.com/oauth/v2/accessToken', data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.VIVIDSYNC_LINKEDIN_REDIRECT_URI,
            'client_id': settings.VIVIDSYNC_LINKEDIN_CLIENT_ID,
            'client_secret': settings.VIVIDSYNC_LINKEDIN_CLIENT_SECRET,
        })

        data = response.json()
        access_token = data.get('access_token')
        print(f"{access_token=}")
        if not access_token:
            return redirect('/error/')  # Handle error scenario

        profile_response = requests.get(
            'https://api.linkedin.com/v2/userinfo',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        
        if profile_response.status_code != 200:
            return redirect('/error/')
        
        profile_data = profile_response.json()
        user = request.user
        if not user:
            return redirect('/error/')

        platform = SocialMediaPlatform.objects.get_or_create(name='Linkedin')[0]
        profile, created = SocialMediaProfile.objects.update_or_create(
            user=user,
            platform=platform,
            profile_id=profile_data.get('sub'),
            defaults={
                'name': profile_data.get('name'),
                'first_name': profile_data.get('given_name'),
                'last_name': profile_data.get('family_name'),
                'handle': profile_data.get('email'),
                'remote_profile_picture' : profile_data.get('picture'),
                'access_token': access_token,
                'token_expires_at': timezone.now() + timezone.timedelta(seconds=data.get('expires_in'))
            }
        )

        return redirect('/me/')  # Redirect after successful processing

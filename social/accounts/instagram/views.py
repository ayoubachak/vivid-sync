
from django.shortcuts import redirect
from django.conf import settings
import requests
from social.models import SocialMediaPlatform, SocialMediaProfile
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect


class InitiateInstagramAuth(APIView):
    def get(self, request, *args, **kwargs):
        oauth_url = f"https://api.instagram.com/oauth/authorize?client_id={settings.VIVIDSYNC_INSTAGRAM_APP_ID}&redirect_uri={settings.VIVIDSYNC_INSTAGRAM_APP_REDIRECT_URI}&scope=user_profile,user_media&response_type=code"
        print("Initialization for code")
        return HttpResponseRedirect(oauth_url)

class InstagramCallback(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if not code:
            return redirect('/error/')  # Handle error scenario

        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return redirect('/login/')  # Redirect to login page or handle as appropriate

        # Exchange code for short-lived access token
        response = requests.post('https://api.instagram.com/oauth/access_token', data={
            'client_id': settings.VIVIDSYNC_INSTAGRAM_APP_ID,
            'client_secret': settings.VIVIDSYNC_INSTAGRAM_APP_SECRET,
            'grant_type': 'authorization_code',
            'redirect_uri': settings.VIVIDSYNC_INSTAGRAM_APP_REDIRECT_URI,
            'code': code,
        })

        data = response.json()
        short_lived_token = data.get('access_token')
        
        if not short_lived_token:
            return redirect('/error/')  # Handle error scenario

        # Exchange short-lived token for long-lived token
        long_lived_token_response = requests.get(
            'https://graph.instagram.com/access_token',
            params={
                'grant_type': 'ig_exchange_token',
                'client_secret': settings.VIVIDSYNC_INSTAGRAM_APP_SECRET,
                'access_token': short_lived_token
            }
        )

        long_lived_data = long_lived_token_response.json()
        long_lived_token = long_lived_data.get('access_token')
        expires_in = long_lived_data.get('expires_in')  # Time in seconds until the token expires

        if not long_lived_token:
            return redirect('/error/')  # Handle error scenario

        # Fetch or create the SocialMediaPlatform for Instagram
        platform, _ = SocialMediaPlatform.objects.get_or_create(name='Instagram')

        # Save to SocialMediaProfile model
        SocialMediaProfile.objects.create(
            user=request.user,
            platform=platform,
            handle='the_instagram_username',
            access_token=long_lived_token,
            token_expires_at=timezone.now() + timezone.timedelta(seconds=expires_in)
        )
        
        return redirect('/me/')  # Redirect to a success page

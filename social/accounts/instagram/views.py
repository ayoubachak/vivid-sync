
from django.shortcuts import redirect
from django.conf import settings
import requests
from social.models import SocialMediaPlatform, SocialMediaProfile
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect


class InitiateInstagramBasicAuth(APIView):
    def get(self, request, *args, **kwargs):
        oauth_url = f"https://api.instagram.com/oauth/authorize?client_id={settings.VIVIDSYNC_INSTAGRAM_APP_ID}&redirect_uri={settings.VIVIDSYNC_INSTAGRAM_APP_REDIRECT_URI}&scope=user_profile,user_media&response_type=code"
        print("Initialization for code")
        return HttpResponseRedirect(oauth_url)

class InstagramBasicCallback(APIView):
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

        user_info_response = requests.get(
            f'https://graph.instagram.com/me?fields=id,username,account_type,media_count&access_token={long_lived_token}'
        )
        user_info_data = user_info_response.json()

        # Fetch or create the SocialMediaPlatform for Instagram
        platform, _ = SocialMediaPlatform.objects.get_or_create(name='Instagram')

        # Save to SocialMediaProfile model
        # Inside InstagramCallback after obtaining the long-lived token and user info
        profile, created = SocialMediaProfile.objects.update_or_create(
            platform=platform,
            handle=user_info_data.get('username'),
            profile_id=user_info_data.get('id'),
            defaults={
                'user': request.user,
                'account_type': user_info_data.get('account_type'),
                'url': f"https://www.instagram.com/{user_info_data.get('username')}/",
                'access_token': long_lived_token,
                'token_expires_at': timezone.now() + timezone.timedelta(seconds=expires_in),
            }
        )
        if created:
            print(f"Created new social media profile for {user_info_data.get('username')}")
        else:
            print(f"Updated social media profile for {user_info_data.get('username')}")


        return redirect('/me/')  # Redirect to a success page


from django.shortcuts import redirect
from django.conf import settings
import requests
from social.models import SocialMediaPlatform, SocialMediaProfile
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
import uuid

class InitiateInstagramBusinesssAuth(APIView):
    def get(self, request, *args, **kwargs):
        state = uuid.uuid4().hex  # Generate a unique state value
        request.session['oauth_state'] = state  # Store in the session for later validation

        oauth_url = (
            f"https://www.facebook.com/dialog/oauth?client_id={settings.VIVIDSYNC_FACEBOOK_APP_ID}"
            f"&redirect_uri={settings.VIVIDSYNC_FACEBOOK_LOGIN_INSTAGRAM_REDIRECT_URI}"
            f"&response_type=code"
            f"&state={state}" 
        )
        return HttpResponseRedirect(oauth_url)


class InstagramBusinessCallback(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if not code:
            return redirect('/error/')  # Handle no code scenario

        returned_state = request.GET.get('state')
        original_state = request.session.get('oauth_state')

        if not returned_state or returned_state != original_state:
            return redirect('/error/')  # State mismatch, possible CSRF attack

        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return redirect('/login/')  # Redirect to login page or handle as appropriate

        # Exchange code for short-lived access token
        response = requests.post('https://graph.facebook.com/v18.0/oauth/access_token', data={
            'client_id': settings.VIVIDSYNC_FACEBOOK_APP_ID,
            'client_secret': settings.VIVIDSYNC_FACEBOOK_APP_SECRET,
            'redirect_uri': settings.VIVIDSYNC_FACEBOOK_LOGIN_INSTAGRAM_REDIRECT_URI,
            'code': code,
        })

        data = response.json()
        short_lived_token = data.get('access_token')
        
        if not short_lived_token:
            return redirect('/error/')  # Handle error scenario

        # Exchange short-lived token for long-lived token
        long_lived_token_response = requests.get(
            'https://graph.facebook.com/v18.0/oauth/access_token',
            params={
                'grant_type': 'fb_exchange_token',
                'client_id': settings.VIVIDSYNC_FACEBOOK_APP_ID,
                'client_secret': settings.VIVIDSYNC_FACEBOOK_APP_SECRET,
                'fb_exchange_token': short_lived_token
            }
        )

        long_lived_data = long_lived_token_response.json()
        long_lived_token = long_lived_data.get('access_token')
        expires_in = long_lived_data.get('expires_in')  # Time in seconds until the token expires

        if not long_lived_token:
            return redirect('/error/')  # Handle error scenario
        
        platform, _ = SocialMediaPlatform.objects.get_or_create(name='Instagram Business / Creator Page')
        print("authenticated successfully")
        
        # Get user's Facebook Pages
        profile, created = SocialMediaProfile.objects.update_or_create(
            platform=platform,
            defaults={
                'user': request.user,
                'access_token': long_lived_token,
                'token_expires_at': timezone.now() + timezone.timedelta(seconds=expires_in),
            }
        )
        
        pages_response = requests.get(
            f'https://graph.facebook.com/v18.0/me/accounts?access_token={long_lived_token}'
        )
        pages_data = pages_response.json()


        print(f"{pages_data=}")
        # Get user's Instagram Business Accounts
        return redirect('/me/')  # Redirect to a success page

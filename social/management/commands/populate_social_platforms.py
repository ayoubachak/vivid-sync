# social/management/commands/populate_social_platforms.py

from django.core.management.base import BaseCommand
from django.conf import settings
from social.models import SocialMediaPlatform

class Command(BaseCommand):
    help = 'Populates Social Media Platforms in the database'

    def handle(self, *args, **kwargs):
        SocialMediaPlatform.objects.update_or_create(
            name='Instagram',
            defaults={
                'base_url': 'https://www.instagram.com/',
                'login_redirect_url': settings.VIVIDSYNC_INSTAGRAM_APP_AUTH_INIT_URI, # this is the first url that the user will be redirected to when clicked to get the necessary code
                'login_callback_url': settings.VIVIDSYNC_INSTAGRAM_APP_REDIRECT_URI # this is the url that the user will be redirected from the third party to when code is received
            }
        )
        self.stdout.write(self.style.SUCCESS('Successfully populated social media platforms'))

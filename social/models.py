# social/models.py

from django.db import models
from users.models import VividUser
from django.utils import timezone
import requests
import re

def social_link_icon_directory_path(instance, filename):
    return f'social_links/{instance.id}/icon/{filename}'

def social_media_platform_icon_directory_path(instance, filename):
    # Replace all non-alphanumeric characters (except for hyphens and underscores) with an underscore
    safe_name = re.sub(r'[^\w\-]', '_', instance.name)
    return f'social_platform_icons/{safe_name}/icon/{filename}'

class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    
    
class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=50, unique=True)
    base_url = models.URLField(max_length=500)
    login_redirect_url = models.URLField(max_length=500, blank=True, null=True)
    login_callback_url = models.URLField(max_length=500, blank=True, null=True)
    icon = models.ImageField(upload_to=social_media_platform_icon_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name

class SocialMediaProfile(models.Model):
    user = models.ForeignKey(VividUser, on_delete=models.CASCADE, related_name='social_media_profiles')
    email = models.EmailField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    profile_id = models.CharField(max_length=255, blank=True, null=True)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    platform = models.ForeignKey(SocialMediaPlatform, on_delete=models.CASCADE, related_name='profiles')
    handle = models.CharField(max_length=255)
    url = models.URLField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='social_profile_pics/', blank=True, null=True)
    remote_profile_picture = models.CharField(max_length=500, blank=True, null=True)
    followers_count = models.IntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_page = models.BooleanField(default=False)
    page_id = models.CharField(max_length=255, blank=True, null=True)
    page_name = models.CharField(max_length=255, blank=True, null=True)
    
    # New fields for OAuth data
    access_token = models.CharField(max_length=500, blank=True, null=True)
    refresh_token = models.CharField(max_length=500, blank=True, null=True)
    token_expires_at = models.DateTimeField(null=True, blank=True)  

    def get_platform_url(self):
        """
        Returns the full URL to the social media profile, if base_url is provided for the platform.
        """
        if self.platform.base_url:
            return f"{self.platform.base_url}/{self.handle}"
        return self.url

    def __str__(self):
        return f"{self.user.username} on {self.platform.name}"
    
    def refresh_access_token(self):
        """
        Refresh the access token for the profile.
        """
        # Example for Instagram ( This will not work, it's just an example yoo )
        if self.platform.name.lower() == 'instagram':
            response = requests.get(
                'https://graph.instagram.com/refresh_access_token',
                params={
                    'grant_type': 'ig_refresh_token',
                    'access_token': self.access_token
                }
            )

            data = response.json()
            if 'access_token' in data:
                self.access_token = data['access_token']
                self.token_expires_at = timezone.now() + timezone.timedelta(seconds=data['expires_in'])
                self.save()


class ExternalUser(models.Model):
    external_id = models.CharField(max_length=255)  # ID used in the external system
    username = models.CharField(max_length=255)
    profile_picture_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    profile = models.ForeignKey(SocialMediaProfile, on_delete=models.CASCADE, related_name='posts')
    external_user = models.ForeignKey(ExternalUser, on_delete=models.SET_NULL, null=True, related_name='posts')
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Post by {self.profile.user.username} on {self.profile.platform.name}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    external_user = models.ForeignKey(ExternalUser, on_delete=models.SET_NULL, null=True, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.external_user.username} on post {self.post.id}"



class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    external_user = models.ForeignKey(ExternalUser, on_delete=models.SET_NULL, null=True, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reply by {self.external_user.username} on comment {self.comment.id}"


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('TikTok', 'TikTok'),
        ('YouTube', 'YouTube'),
        ('LinkedIn', 'LinkedIn'),
        # Add more as needed
    ]

    user = models.ForeignKey(VividUser, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=100, choices=PLATFORM_CHOICES)
    url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.user.username}'s {self.platform} link"
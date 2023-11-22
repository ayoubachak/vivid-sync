from django.db import models
from social.models import SocialMediaProfile

class Content(models.Model):
    profile = models.ForeignKey(SocialMediaProfile, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    posted_date = models.DateTimeField()
    url = models.URLField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)
    video = models.FileField(upload_to='content_videos/', blank=True, null=True)
    status = models.CharField(max_length=50, default='draft')
    scheduled_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.profile.platform.name}"


class ContentPlatformStatus(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='platform_statuses')
    platform = models.ForeignKey(SocialMediaProfile, on_delete=models.CASCADE)
    is_posted = models.BooleanField(default=False)
    posted_at = models.DateTimeField(null=True, blank=True)
    platform_specific_data = models.JSONField(blank=True, null=True)  # For storing any platform-specific response or data

    def __str__(self):
        return f"Status for {self.content.title} on {self.platform.platform.name}"

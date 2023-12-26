from django.db import models

from django.db import models
from users.models import VividUser
from django.db import models

def organization_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/images/profile_pic/<filename>
    return f'organizations/{instance.id}/images/image/{filename}'
def organization_banner_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/images/profile_pic/<filename>
    return f'organizations/{instance.id}/images/banner/{filename}'


class Organization(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(VividUser, on_delete=models.CASCADE, related_name='administered_organizations')
    image = models.ImageField(upload_to=organization_image_directory_path, blank=True, null=True)
    banner = models.ImageField(upload_to=organization_banner_directory_path, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    organization_size = models.CharField(max_length=100, blank=True, null=True)
    organization_type = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    year_founded = models.IntegerField(blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    industries = models.ManyToManyField('Industry', related_name='organizations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

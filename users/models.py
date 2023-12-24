from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from django.apps import apps


class AccountType(models.TextChoices):
    INFLUENCER = 'Influencer', _('Influencer')
    CONTENT_CREATOR = 'Content Creator', _('Content Creator')
    ORGANIZATION = 'Organization', _('Organization')

class GenderChoices(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')

class VividUser(AbstractUser):        


    profile_picture = models.ImageField(upload_to='media/images/profile_pics/', blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    verification_code = models.CharField(max_length=6, blank=True)
    verification_token = models.CharField(max_length=100, blank=True)
    agreed_to_terms = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=2,
        choices=GenderChoices.choices,
        default=None,  
        null=True,  # Allows the field to be null
        blank=True,  # Allows the form to be saved without a value
    )
    account_type = models.CharField(
        max_length=50,
        choices=AccountType.choices,
        default=None,
        null=True,
        blank=True
    )
    profile_completed = models.BooleanField(default=False)
    hashtags = models.ManyToManyField('social.Hashtag', related_name='users')

    def info(self):
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "profile_picture": self.profile_picture.url if self.profile_picture else None,
            "bio": self.bio
        }
    
    def save(self, *args, **kwargs):
        if not self.verification_code:
            # Generate a random 6 digit code
            self.verification_code = get_random_string(length=6, allowed_chars='1234567890')
        if not self.verification_token:
            # Generate a unique token
            self.verification_token = get_random_string(length=100)
        super().save(*args, **kwargs)
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string


class VividUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    verification_code = models.CharField(max_length=6, blank=True)
    verification_token = models.CharField(max_length=100, blank=True)
    agreed_to_terms = models.BooleanField(default=False)
    
    # create a function info to display the user info (the email, the first name, the last name, the username, the profile picture, the bio) in the form of a dict
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
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class VividUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
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
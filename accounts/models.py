from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Inherits username, email, password, first_name, and last_name
    age = models.PositiveIntegerField(null=True, blank=True)
    is_parent = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.username

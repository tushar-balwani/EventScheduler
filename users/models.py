from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
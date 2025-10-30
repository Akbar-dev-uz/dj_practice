from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    phone = models.CharField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='profile_img/', null=True, blank=True)

    def __str__(self):
        return self.username

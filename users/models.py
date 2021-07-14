
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from .manager import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import message, send_mail
import uuid

from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def name(self):
        return self.first_name + ' ' + self.last_name


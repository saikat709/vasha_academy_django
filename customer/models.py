import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    fullname = models.CharField(max_length=100, null=False, blank=False, unique=False)
    number = models.CharField(max_length=15, null=False, blank= False, unique=False)
    is_verified = models.BooleanField(default=False, null=False)


class Profile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='profile')
    number = models.CharField(max_length=50, null=True)
    fullname = models.CharField(max_length=100, null=True)


class LoginInfo(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    using_app = models.BooleanField(default=False, null=False)
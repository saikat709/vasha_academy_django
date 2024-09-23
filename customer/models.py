
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class examineeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    number = models.CharField(max_length=50, null=True)
    fullname = models.CharField(max_length=100, null=True)

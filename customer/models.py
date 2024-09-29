import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ManyToManyField


class CustomerManager(BaseUserManager):
    def create_user(self, number, password=None, **extra_fields):
        if not number:
            raise ValueError('The Email field must be set')
        number = self.normalize_email(number)
        user = self.model(number=number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(number, password, **extra_fields)



class Customer(AbstractUser):
    username = models.CharField(max_length=1, null=True, unique=False)
    fullname = models.CharField(max_length=100, null=False, blank=False, unique=False)
    number = models.CharField(max_length=15, null=False, blank= False, unique=True)
    is_verified = models.BooleanField(default=False, null=False)
    # courses = ManyToManyField(Course, null=True, blank=True, related_name="customers")
    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []
    objects = CustomerManager()

    def __str__(self):
        return f"Customer[{self.number}]"


class Profile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='profile')
    number = models.CharField(max_length=50, null=True)
    fullname = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Profile[{self.number}]"


class LoginInfo(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    using_app = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"LoginInfo[{self.token}]"
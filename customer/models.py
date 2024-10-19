import uuid

from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models

from vashaacademy.utils import get_unique_filename


# class CustomerManager(BaseUserManager):
#     def create_user(self, number, password=None, **extra_fields):
#         if not number:
#             raise ValueError('The Email field must be set')
#         number = number
#         user = self.model(number=number, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, number, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(number, password, **extra_fields)



class Customer(AbstractUser):
    name = models.CharField(max_length=100, null=False, blank=False, unique=False)
    is_verified = models.BooleanField(default=False, null=False)
    is_email = models.BooleanField(default=True)
    picture = models.ImageField(upload_to=get_unique_filename, null=True, blank=True)
    # USERNAME_FIELD = 'number'
    # REQUIRED_FIELDS = []
    # objects = CustomerManager()

    def __str__(self):
        return f"Customer[{self.name} -- {self.username}]"


class LoginInfo(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    using_app = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"LoginInfo[{self.token}]"


# class Profile(models.Model):
#     user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
#     number = models.CharField(max_length=50, null=True)
#     fullname = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return f"Profile[{self.number}]"

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomModel(AbstractUser):
    nickname = models.CharField(max_length=10)
    school = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)

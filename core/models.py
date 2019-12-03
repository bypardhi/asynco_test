from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
# from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Data(models.Model):
    number = models.CharField(max_length=100)
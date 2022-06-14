from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    location = models.CharField(max_length=100)

class Event(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    flexible_start_time = models.TimeField()
    flexible_end_time = models.TimeField()
    coach = models.BooleanField()
    price = models.IntegerField()

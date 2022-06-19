from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    location = models.CharField(max_length=100)

class Organiser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

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
    coach_user = models.ForeignKey(User, related_name='events', on_delete=models.DO_NOTHING, null=True, blank=True)
    sport = models.CharField(max_length=50) 
    role = models.CharField(max_length=50)
    recurring = models.BooleanField(default=False)
    offers = models.ManyToManyField(User, related_name='applied_events', blank=True)

from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = 40

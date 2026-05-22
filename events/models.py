from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name=models.CharField(max_length=100)
    country_name=models.CharField(max_length=100)
    year=models.IntegerField()
    num=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name} - ({self.country_name})"

class Event(models.Model):
    name=models.CharField(max_length=100)
    date_time=models.DateTimeField()
    poster=models.ImageField(upload_to='posters/', blank=True,null=True)
    creator=models.ForeignKey(User, on_delete=models.CASCADE)
    bands=models.ManyToManyField(Band, blank=True)
    is_outdoor=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - ({self.date_time})"
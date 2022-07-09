from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name
from statistics import mode
from urllib import request
from django.db import models
from django.contrib.auth.models import User





class Topic(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

        
class Room(models.Model):
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True )
    Host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    roomType = models.CharField(max_length = 50)
    participants = models.ManyToManyField(User ,related_name='participants', blank = True) 
    description = models.TextField(null = True , blank=True)
    name = models.CharField(max_length = 200, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

class message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.body[0:50]

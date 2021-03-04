from django.db import models
from django.contrib.auth.models import User


class ChatModel(models.Model):
    room = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    user = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.room
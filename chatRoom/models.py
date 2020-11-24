from django.db import models
from django.contrib.auth.models import User


class ChatModel(models.Model):
    room = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.room
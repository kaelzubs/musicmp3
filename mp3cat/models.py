from turtle import title
from django.db import models

# Create your models here.

class HomeModel(models.Model):
    title = models.CharField(max_length=500)
    audio_id = models.CharField(max_length=500)

    def __str__(self):
        return self.title

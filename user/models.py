from django.contrib.auth.models import User
from django.db import models
from YouTube import settings
from video.models import Playlist

class Account(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date=models.DateField(blank=True)
    bio=models.CharField(max_length=150,blank=True)
    prof_pic=models.URLField(blank=True)
    playlists = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    gender=models.CharField(max_length=10,choices=(('male','male'),('female','female')))
    def __str__(self):
        return f"{self.name},{self.surname}"

from django.conf import settings
from django.db import models
from user.models import User


class Comment(models.Model):
    text = models.CharField(max_length=250)
    user = models.ManyToManyField(settings.YOUTUBE_ACCOUNT,related_name="comment",blank=True)

class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.FileField()
    video = models.FileField()
    comments = models.ManyToManyField(Comment,blank=True)

class Playlist(models.Model):
    name = models.CharField(max_length=50)
    video =models.ManyToManyField(Video)
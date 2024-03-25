from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime



User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank_profile_pictre.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    user = models.CharField(max_length=100)
    image =  models.ImageField(upload_to='post_images')
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=300)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(User,related_name='user_like', blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.user


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    


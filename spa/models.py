# comments/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    user_name = models.CharField(max_length=64)
    email = models.EmailField()
    avatar_url = models.URLField(blank=True, null=True)
    text = models.TextField(max_length=1024)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:64]

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=64)
    email = models.EmailField()
    text = models.TextField(max_length=512)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:64]

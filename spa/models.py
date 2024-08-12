from pathlib import Path
from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Post(models.Model):
    user_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    avatar_url = models.URLField(blank=True, null=True, max_length=128)
    text = models.TextField(max_length=1024)
    created_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.text[:64]


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=64)
    email = models.EmailField()
    text = models.TextField(max_length=512)
    created_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.text[:64]


def upload_file(instance, filename):
    # upload_to = Path(instance.user_post.user_name) if instance.user_post else Path('images')
    upload_to = Path('files')
    ext = Path(filename).suffix
    if ext in [".txt", ".png", ".jpeg", ".jpg", ".gif"]:
        new_filename = f"{uuid4().hex}{ext}"
        return str(upload_to / new_filename)
    return "The extention of upload files must be .txt, .png, .jpeg, .jpg, .gif."


def validate_file_size(value):
    filesize = value.size
    if filesize > 1_048_576:
        return "The maximum file size that can be uploaded is 1MB."
    return None


class File(models.Model):
    path = models.ImageField(upload_to=upload_file, validators=[validate_file_size])
    user_post = models.OneToOneField('Post', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Picture for {self.user_post.user_name}' if self.user_post else 'No Post Linked'

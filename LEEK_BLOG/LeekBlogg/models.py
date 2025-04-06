from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class CreateAccount(models.Model):
  user_name = models.CharField(max_length=200)
  age = models.FloatField()
  phone_number = models.CharField(max_length=20)
  password = models.CharField(max_length=128)
  gender = models.TextField()

class PostContent(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)
  content = models.TextField()
  date_created = models.DateTimeField(default=timezone.now)
  likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_details')
  bio =models.TextField(blank=True)
  profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

  def __str__(self):
    return f'{self.user.username} Profile'

class Likes(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
  post = models.ForeignKey(PostContent, on_delete=models.CASCADE, related_name='liked')
  liked_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commented_on_post')
  post = models.ForeignKey(PostContent, related_name='comment_on_post', on_delete=models.CASCADE)
  content = models.TextField()
  commented_at = models.DateTimeField(auto_now_add=True)
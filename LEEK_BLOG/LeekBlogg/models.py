from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CreateAccount(models.Model):
  user_name = models.CharField(max_length=250)
  age = models.IntegerField(max_length=150)
  gender = models.CharField(max_length=220)
  phone_number = models.IntegerField(max_length=220)
  marital_stat = models.CharField(max_length=270)
  password = models.CharField(max_length=150)

class PostContent(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  content = models.CharField(max_length=250)
  date_created = models.DateTimeField()
  likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
from rest_framework import serializers
from .models import CreateAccount, PostContent, Comment, Likes, Profile

class SignUpSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreateAccount
    fields = ['user_name', 'age', 'gender', 'phone_number', 'password']

  def validate(self, data):
    if len(data['password']) < 8:
      raise serializers.ValidationError("password needs to be atleast 8 characters long")
    return data
  
class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['user', 'bio', 'profile_picture']

class LikesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Likes
    fields = ['author', 'post', 'liked_at']

class CommentSerializer(serializers.ModelSerializer):
  likes = LikesSerializer(many=True, read_only=True)

  class Meta:
    model = Comment
    fields = ['id', 'author', 'content', 'commented_at', 'likes']
  
  def to_representation(self, instance):
        data = super().to_representation(instance)
        data['comment_count'] = instance.post.comment_set.count()  # Assuming PostContent has a reverse relation to comments
        return data

class PostContentSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = PostContent
    fields = ['author', 'post', 'content', 'date_created', 'comments']
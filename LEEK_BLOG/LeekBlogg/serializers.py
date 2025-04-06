from rest_framework import serializers
from .models import CreateAccount, PostContent

class SignUpSerializer(serializers.ModelSerializer):
  class meta:
    model = CreateAccount
    Fields = ['user_name', 'age', 'gender', 'phone_number', 'marital_stat', 'password']

  def validate(self, data):
    if len(data['password']) < 8:
      raise Serializers.ValidationError("password needs to be atleast 8 characters long")
    return data

class PostContentSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostContent
    fields = ['title', 'content']
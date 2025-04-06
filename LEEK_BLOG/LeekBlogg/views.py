from django.shortcuts import render
from rest_framework import generics
from .models import CreateAccount
from .serializers import SignUpSerializer 

# Create your views here.
class AccountCreateAPIView(generics.ListCreateAPIView):
  queryset = CreateAccount.objects.all()
  serializer_class = SignUpSerializer

class AccountUpdateView(generics.UpdateApiView):
  queryset = CreateAccount.objects.all()
  serializer_class = SignUpSerializer

class AccountDetailView(generics.CreateAPIView):
  queryset = CreateAccount.objects.all()
  serializer_class = SignUpSerializer
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CreateAccount, PostContent, Likes, Comment, Profile
from .serializers import SignUpSerializer, PostContentSerializer, LikesSerializer, CommentSerializer, ProfileSerializer 

# Create your views here.
class AccountCreateAPIView(viewsets.ModelViewSet):
  queryset = CreateAccount.objects.all()
  serializer_class = SignUpSerializer

class PostCreateAPIView(viewsets.ModelViewSet):
  queryset = PostContent.objects.all()
  serializer_class = PostContentSerializer
  permission_class = [permissions.IsAuthenticatedOrReadOnly]

  @action(detail=True, methods=['post'], permission_classes=permissions.IsAuthenticated)
  def like(self, request):
    post = self.get_object()
    like, created = Likes.objects.get_or_create(user=request.user, post=post)
    if not created:
      return Response({'message': 'Already liked'}, status=status.HTTP_404_BAD_REQUEST)
    return Response({'message': 'Liked successfully'})
  
  @action(detail=True, methods=['post'], permission_classes=permissions.IsAuthenticated)
  def comment(self, request,):
    post = self.get_object()
    content = request.data.get('content')
    if not content:
      return Response({'error': 'comment content is required'}, status=400)
    Comment.objects.create(post=post, author=request.user, content=content)
    return Response({'message': 'comment added!'})

class ProfileAPIView(viewsets.ModelViewSet):
  quueryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LikesViewSet(viewsets.ModelViewSet):
  queryset = Likes.objects.all()
  serializer_class = LikesSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentAPIViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_classes = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
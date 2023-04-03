from django.shortcuts import render
from post.models import Post
from rest_framework import viewsets

from r_account.models import CustomUser
from .serializer import UserSerializer
from .serializer import PostSerializer
from rest_framework.permissions import AllowAny
# Create your views here.


class UserApiView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]




class PostApiView(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

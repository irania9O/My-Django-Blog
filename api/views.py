from django.shortcuts import render
from account.models import User
from blog.models import Article
from .serializers import Userserializer, Articleserializer
from .permissions import (
    IsSuperUser,
    IsAuthorOrReadOnly
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [IsSuperUser]

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [IsSuperUser]

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer
    permission_classes = [IsAuthorOrReadOnly]

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer
    permission_classes = [IsAuthorOrReadOnly]
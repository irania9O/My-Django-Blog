from django.shortcuts import render
# from account.models import User
from django.contrib.auth import get_user_model
from blog.models import Article
from .serializers import Userserializer, Articleserializer
from .permissions import (
    IsSuperUser,
    IsAuthorAndDraftOrReadOnly
)
from rest_framework.viewsets import ModelViewSet

class UserViewSET(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = Userserializer
    permission_classes = [IsSuperUser]  
    ordering_fields = ['special_user', 'date_joined', 'last_login']
    search_fields = ['username', 'email', 'first_name', 'last_name']


class ArticleViewSET(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Articleserializer
    permission_classes = [IsAuthorAndDraftOrReadOnly]
    filterset_fields = ['status', 'author']
    ordering_fields = ['publish', 'status', 'updated', 'hits__count']
    ordering = ['-publish']
    search_fields = [
                        'title',
                        'description',
                        'catagory__title',
                        'author__username',
                        'author__first_name',
                        'author__last_name', 
                    ]
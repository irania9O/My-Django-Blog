from django.shortcuts import render
# from account.models import User
from django.contrib.auth import get_user_model
from blog.models import Article
from .serializers import Userserializer, Articleserializer
from .permissions import (
    IsSuperUser,
    IsAuthorAndDraftOrReadOnly
)
# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView
# )

from rest_framework.viewsets import ModelViewSet

class UserViewSET(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = Userserializer
    permission_classes = [IsSuperUser]  


class ArticleViewSET(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Articleserializer
    permission_classes = [IsAuthorAndDraftOrReadOnly]
    
    # def get_permissions(self):
    #     if self.action in ['list']:
    #         permission_classes = [IsAuthorOrReadOnly]
    #     else:
    #         permission_classes = [IsAuthorOrReadOnly]

    #     return [permission() for permission in permission_classes]
        

# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = Userserializer
#     permission_classes = [IsSuperUser]

# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = Userserializer
#     permission_classes = [IsSuperUser]

# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = Articleserializer
#     permission_classes = [IsAuthorOrReadOnly]

# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = Articleserializer
#     permission_classes = [IsAuthorOrReadOnly]
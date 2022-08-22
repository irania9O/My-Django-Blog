from django.shortcuts import render
from account.models import User
from .serializers import Userserializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    # permission_classes = [IsSuperUser]

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    # permission_classes = [IsSuperUser]
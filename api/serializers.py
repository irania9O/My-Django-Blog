from rest_framework import serializers
# from account.models import User
from django.contrib.auth import get_user_model
from blog.models import Article

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__" 


class Articleserializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
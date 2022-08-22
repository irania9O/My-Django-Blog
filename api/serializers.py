from rest_framework import serializers
from account.models import User
from blog.models import Article

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" 


class Articleserializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
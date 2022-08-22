from rest_framework.serializers import ModelSerializer
# from account.models import User
from django.contrib.auth import get_user_model
from blog.models import Article


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__" 


class ArticleSerializer(ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Article
        fields = "__all__"
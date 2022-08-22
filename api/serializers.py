from rest_framework.serializers import ModelSerializer, SerializerMethodField
# from account.models import User
from django.contrib.auth import get_user_model
from blog.models import Article


# class AuthorSerializer(ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ["id", "username", "first_name", "last_name"]

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__" 


class ArticleSerializer(ModelSerializer):
    # author = AuthorSerializer()

    def get_author(self, obj):
        return {
            "pk": obj.author.pk,
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
        }
    author = SerializerMethodField("get_author") 
    class Meta:
        model = Article
        fields = "__all__"
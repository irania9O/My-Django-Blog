from django.urls import path, include
from .views import (
    UserList,
    UserDetail,
    ArticleList,
    ArticleDetail
    )

app_name = "api"

urlpatterns = [
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>', UserDetail.as_view(), name="user-detail"),

    path('articles/', ArticleList.as_view(), name="article-list"),
    path('articles/<int:pk>', ArticleDetail.as_view(), name="article-detail"),
]
 
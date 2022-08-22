from django.urls import path, include
from .views import (
    UserList,
    UserDetail
    )

app_name = "api"

urlpatterns = [
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>', UserDetail.as_view(), name="user-detail"),
]
 
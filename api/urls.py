from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSET,
    ArticleViewSET
    )

app_name = "api"

router = routers.SimpleRouter()
router.register(r'users', UserViewSET)
router.register(r'articles', ArticleViewSET)

# urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls))
]


# urlpatterns = [
#     path('users/', UserList.as_view(), name="user-list"),
#     path('users/<int:pk>', UserDetail.as_view(), name="user-detail"),

#     path('articles/', ArticleList.as_view(), name="article-list"),
#     path('articles/<int:pk>', ArticleDetail.as_view(), name="article-detail"),
# ]
 
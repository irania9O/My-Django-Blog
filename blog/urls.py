from django.urls import path
from .views import ArticleList, ArticleDetail, CatagoryList, AuthorList

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name= "home"),
    path('page/<int:page>', ArticleList.as_view(), name= "home"),
    path('article/<slug:slug>' , ArticleDetail.as_view(), name= "detail"),
    path('catagory/<slug:slug>' , CatagoryList.as_view(), name= "catagory"),
    path('catagory/<slug:slug>/page/<int:page>' , CatagoryList.as_view(), name= "catagory"),
    path('author/<slug:username>' , AuthorList.as_view(), name= "author"),
    path('author/<slug:username>/page/<int:page>' , AuthorList.as_view(), name= "author")
]
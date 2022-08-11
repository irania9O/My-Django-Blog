from django.urls import path
from .views import home, detail, catagory

app_name = "blog"
urlpatterns = [
    path('', home, name= "home"),
    path('page/<int:page>', home, name= "home"),
    path('article/<slug:slug>' , detail, name= "detail"),
    path('catagory/<slug:slug>' , catagory, name= "catagory"),
    path('catagory/<slug:slug>/page/<int:page>' , catagory, name= "catagory")
]
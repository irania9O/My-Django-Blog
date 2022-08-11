from django.shortcuts import render, get_object_or_404
from .models import Article, Catagory

def home(request):
    context = {
        "articles": Article.objects.published()
    }
    return render(request, "blog/home.html", context)

def detail(request, slug):
    context = {
        "article": get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, "blog/detail.html", context)

def catagory(request, slug):
    context = {
        "catagory": get_object_or_404(Catagory, slug=slug, status=True)
    }
    return render(request, "blog/catagory.html", context)
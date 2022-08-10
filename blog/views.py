from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    context = {
        "articles": Article.objects.filter(status='p').order_by('-publish')
    }
    return render(request, "blog/home.html", context)

def detail(request, slug):
    context = {
        "article": get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, "blog/detail.html", context)

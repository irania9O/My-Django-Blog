from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Catagory

def home(request, page=1):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 5)
    articles = paginator.get_page(page)
    context = {
        "articles": articles
    }
    return render(request, "blog/home.html", context)

def detail(request, slug):
    context = {
        "article": get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, "blog/detail.html", context)

def catagory(request, slug, page=1):
    catagory = get_object_or_404(Catagory, slug=slug, status=True)
    articles_list = catagory.articles.published()
    paginator = Paginator(articles_list, 5)
    articles = paginator.get_page(page)
    context = {
        "catagory": catagory,
        "articles": articles
    }
    return render(request, "blog/catagory.html", context)
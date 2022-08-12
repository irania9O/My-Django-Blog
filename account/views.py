from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Article


class ArticleList(LoginRequiredMixin, ListView):
    queryset = Article.objects.all()
    template_name = 'registration/home.html'
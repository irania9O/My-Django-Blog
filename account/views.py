from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import ProfileForm
from .mixins import (
    FieldsMixin, 
    FormValidMixin, 
    AuthorAccessMixin,
    AuthorsAccessMixin,
    SuperUserAccessMixin
    )
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView
    )
from blog.models import Article
from .models import User

class ArticleList(AuthorsAccessMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(AuthorsAccessMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Article
    template_name = 'registration/article-create-update.html'


class ArticleUpdate(AuthorAccessMixin,FormValidMixin, FieldsMixin, UpdateView):
    model = Article
    template_name = 'registration/article-create-update.html'


class ArticleDelete(SuperUserAccessMixin,DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = 'registration/article_confirm_delete.html'

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('account:profile')
    template_name = 'registration/profile.html'
    form_class = ProfileForm

    def get_object(self):
        return User.objects.get(pk= self.request.user.pk)

class Login(LoginView):
    def get_success_url(self) -> str:
        user = self.request.user

        if user.is_superuser or user.is_author:
            return reverse_lazy('account:home')
        else:
            return reverse_lazy('account:profile')
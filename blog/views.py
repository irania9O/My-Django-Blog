# from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# from account.models import User
from django.contrib.auth import get_user_model
from account.mixins import AuthorAccessMixin
from .models import Article, Catagory

# def home(request, page=1):
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 5)
#     articles = paginator.get_page(page)
#     context = {
#         "articles": articles
#     }
#     return render(request, "blog/home.html", context)

class ArticleList(ListView):
    # model = Article
    # template_name = "blog/home.html"
    # context_object_name = "articles"
    
    queryset = Article.objects.published()
    paginate_by = 5

#----------------------------------------
# def detail(request, slug):
#     context = {
#         "article": get_object_or_404(Article.objects.published(), slug=slug)
#     }
#     return render(request, "blog/detail.html", context)

class ArticleDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get("slug")
        article = get_object_or_404(Article.objects.published(), slug=slug)

        ip_address =  self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)

        return article

#----------------------------------------
# def catagory(request, slug, page=1):
#     catagory = get_object_or_404(Catagory, slug=slug, status=True)
#     articles_list = catagory.articles.published()
#     paginator = Paginator(articles_list, 5)
#     articles = paginator.get_page(page)
#     context = {
#         "catagory": catagory,
#         "articles": articles
#     }
#     return render(request, "blog/catagory.html", context)

class CatagoryList(ListView):
    paginate_by = 5
    template_name = "blog/catagory_list.html"

    def get_queryset(self):
        global catagory
        slug = self.kwargs.get("slug")
        catagory = get_object_or_404(Catagory.objects.active(), slug=slug)
        return catagory.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catagory'] = catagory
        return context


class AuthorList(ListView):
    paginate_by = 5
    template_name = "blog/author_list.html"

    def get_queryset(self):
        global author
        username = self.kwargs.get("username")
        author = get_object_or_404(get_user_model(), username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
    

class ArticlePreview(AuthorAccessMixin, DetailView):
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Article, pk=pk)

class SearchList(ListView):
	paginate_by = 5
	template_name = 'blog/search_list.html'

	def get_queryset(self):
		search = self.request.GET.get('q')
		return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['search'] = self.request.GET.get('q')
		return context

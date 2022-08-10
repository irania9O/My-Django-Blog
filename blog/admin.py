from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'jpublish', 'status'] 
    list_filter = ['publish', 'status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', 'publish']
    
admin.site.register(Article, ArticleAdmin)

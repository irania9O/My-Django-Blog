from django.contrib import admin
from .models import Article, Catagory, SiteSetting


class SiteSettingsAdmin(admin.ModelAdmin):
    # Create a default object on the first page of SiteSettingsAdmin with a list of settings
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        # be sure to wrap the loading and saving SiteSettings in a try catch,
        # so that you can create database migrations
        try:
            SiteSetting.load().save()
        except Exception:
            pass
 
    # prohibit adding new settings
    def has_add_permission(self, request, obj=None):
        return False
 
    # as well as deleting existing
    def has_delete_permission(self, request, obj=None):
        return False
 
 
admin.site.register(SiteSetting, SiteSettingsAdmin)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'slug', 'status'] 
    list_filter = ['status']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)} 
    
admin.site.register(Catagory, CatagoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'jpublish', 'status', 'catagoy_to_list'] 
    list_filter = ['publish', 'status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', 'publish']
    
    def catagoy_to_list(self, obj):
        catagoties = []
        for catagory in obj.catagory.all():
            catagoties.append(catagory.title)
        
        if len(catagoties) == 0:
            return "بدون دسته بندی"
        else:
            return "، ".join(catagoties)

    catagoy_to_list.short_description = "دسته بندی"


admin.site.register(Article, ArticleAdmin)

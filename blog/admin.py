from django.contrib import admin, messages
from django.utils.translation import ngettext
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

#-------------------------------------------------------------
@admin.action(description='فعال کردن دسته بندی های انتخاب شده')
def make_active(modeladmin, request, queryset):
    updated = queryset.update(status=True)
    modeladmin.message_user(request, ngettext(
                '%d دسته بندی فعال شد.',
                '%d دسته بندی ها فعال شدند.',
                updated,
            ) % updated, messages.SUCCESS)

@admin.action(description='غیر فعال کردن دسته بندی های انتخاب شده')
def make_diactive(modeladmin, request, queryset):
    updated = queryset.update(status=False)
    modeladmin.message_user(request, ngettext(
                '%d دسته بندی  غیر فعال شد.',
                '%d دسته بندی ها غیر فعال شدند.',
                updated,
            ) % updated, messages.SUCCESS)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'parent', 'slug', 'status'] 
    list_filter = ['status']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)} 
    actions = [make_active, make_diactive]
    
admin.site.register(Catagory, CatagoryAdmin)

#-------------------------------------------------------------
@admin.action(description='انتشار مقالات انتخاب شده')
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
                '%d مقاله منتشر شد.',
                '%d مقاله منتشر شدند.',
                updated,
            ) % updated, messages.SUCCESS)

@admin.action(description='پیش نویس شدن مقالات انتخاب شده')
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
                '%d مقاله پیش‌نویس شد.',
                '%d مقاله پیش‌نویس شدند.',
                updated,
            ) % updated, messages.SUCCESS)
            
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail_tag', 'slug', 'author', 'jpublish', 'status', 'catagoy_to_list'] 
    list_filter = ['publish', 'status', 'author']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', 'publish']
    actions = [make_published, make_draft]
    
    def catagoy_to_list(self, obj):
        catagoties = []
        for catagory in obj.catagory.active():
            catagoties.append(catagory.title)
        
        if len(catagoties) == 0:
            return "بدون دسته بندی"
        else:
            return "، ".join(catagoties)

    catagoy_to_list.short_description = "دسته بندی"

admin.site.register(Article, ArticleAdmin)

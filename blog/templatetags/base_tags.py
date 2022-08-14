from ..models import SiteSetting, Catagory, Article
from django import template
from django.utils import timezone
from django.db.models import Count, Q
from dateutil.relativedelta import relativedelta
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.simple_tag
def site_name():
    return SiteSetting.objects.get(pk=1).site_name

@register.simple_tag
def site_header():
    return SiteSetting.objects.get(pk=1).site_header

    
@register.simple_tag
def site_description():
    return SiteSetting.objects.get(pk=1).site_description

@register.simple_tag
def site_image():
    return SiteSetting.objects.get(pk=1).image.url

@register.inclusion_tag("blog/partials/catagory_navbar.html")
def catagory_navbar():
    return {
        "catagories": Catagory.objects.filter(status=True)
    }

@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": f"account:{link_name}",
        "content": content,
        "classes": classes
    }

@register.inclusion_tag("blog/partials/sidebar.html")
def popular_articles():
	last_month = timezone.now() - relativedelta(months=1)
	return {
        "title" : "مقالات پربازدید ماه",
		"articles": Article.objects.published().annotate(
			count=Count('hits', filter=Q(articlehit__created__gt=last_month))
		).order_by('-count', '-publish')[:5]
	}

@register.inclusion_tag("blog/partials/sidebar.html")
def hot_articles():
	last_month = timezone.now() - relativedelta(months=1)
	content_type_id = user_type = ContentType.objects.get(app_label='blog', model='article').id
	return {
        "title": "مقالات داغ ماه",
		"articles": Article.objects.published().annotate(
			count=Count('comments', filter=Q(comments__posted__gt=last_month) and Q(comments__content_type_id=content_type_id))
		).order_by('-count', '-publish')[:5],	
	}

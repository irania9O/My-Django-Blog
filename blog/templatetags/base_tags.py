from django import template
from ..models import SiteSetting, Catagory

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
def link(request, link_name, content):
    return {
        "request": request,
        "link_name": link_name,
        "link": f"account:{link_name}",
        "content": content
    }
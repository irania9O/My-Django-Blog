from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("Hello World!")

def api(request):
    data = {
        "title": "مقاله اول",
        "id": 20,
        "slug": "first-article"
    }
    return JsonResponse(data)
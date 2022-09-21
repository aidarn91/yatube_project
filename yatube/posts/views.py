from django.shortcuts import render

from django.http import HttpResponse

# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Посты по группам
def group_posts(request, slug):
    return HttpResponse(f'Посты {slug}')
# Create your views here.
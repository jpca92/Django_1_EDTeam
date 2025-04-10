from django.shortcuts import render
from django.http import JsonResponse
from .models import Curso

# Create your views here.

def index(request):
    context = {
        'status': True,
        'content': 'my first API'
    }
    return JsonResponse(context)


def course (request):
    courses_list = Curso.objects.all()
    context = {
        'status': True,
        'content': list(courses_list.values())
    }
    return JsonResponse(context)


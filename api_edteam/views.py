from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def index(request):
    context = {
        'status': True,
        'content': 'my first API'
    }
    return JsonResponse(context)



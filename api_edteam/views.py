import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework import serializers

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

@csrf_exempt
def post_course(request):
    
    json_data = json.loads(request.body)
    
    title = json_data['title']
    description = json_data['description']
    image = json_data['image']
    
    new_course = Curso.objects.create(
        title=title,
        description=description,
        image=image
    )
    
    new_dicc = {
        'id':new_course.id,
        'title':new_course.title,
        'description':new_course.description,
        'imagen':new_course.image
    }
    
    context = {
        'status':True,
        'content':new_dicc
    }
    
    return JsonResponse(context)

#Django rest framework
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class CourseList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CourseSerializer
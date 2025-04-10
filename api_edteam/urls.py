from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.course, name='course'),
    path('new_course/', views.post_course, name='post_course'),
    path('cpurse_drf', views.CourseList.as_view(),name='course_drf'),

    
]
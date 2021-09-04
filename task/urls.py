from django.urls import  path
from django.http import HttpResponse
from django.contrib import admin
from . import views


urlpatterns = [
    path( '', views.index,name='index'),
    path( 'home/', views.home,name='home'),
    path( 'update/<str:pk>/', views.update_task,name='update_task'),
   
]
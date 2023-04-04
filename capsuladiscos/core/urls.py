#from django.contrib import admin
from django.urls import path, include
#from core import views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('about-nos/', views.about, name="about"), #url automatizada soporta cualquier nombre
]
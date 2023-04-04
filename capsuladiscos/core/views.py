#from django.shortcuts import render
from django.urls import include
from django.http import HttpResponseRedirect
include('catalogo.urls')

#def home(request):
#    return render(request,"core/home.html")
def home(request):
        return HttpResponseRedirect("catalogo") #REDIRECCIONA HOME AL CATÁLOGO*************

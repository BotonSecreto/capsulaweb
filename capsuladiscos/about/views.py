from django.shortcuts import render
from .models import Nosotros #importar el modelo
# Create your views here.
def about(request):
    nosotros = Nosotros.objects.all() #recupera todos los objetos de la clase
    #*****ruta actualizada al MVT que
    return render(request, "about/about.html",{'nosotros':nosotros}) #Inyecta datos en página html
    #**************

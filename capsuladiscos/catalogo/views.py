from django.shortcuts import render, get_object_or_404
from .models import Disco, Banda, IntegranteBanda, Musico, ProduccionDisco #importar el modelo
# Create your views here.
def catalogo(request):
    #recupera todos los objetos de las clases
    discos = Disco.objects.all().order_by('-fechaDisco','banda','titulo') #order by descendente para fecha y ascendente el resto
    #*****ruta actualizada al MVT que
    return render(request, "catalogo/catalogo.html",{'discos':discos}) #Inyecta datos en página html
    #**************

def disco(request, disco_id):
    disco = get_object_or_404(Disco, id=disco_id) #evitar el error 404 por pág desconocida con "get"
    #disco = get_object_or_404(Disco.objects.all().order_by('-fechaDisco'), id=disco_id) #evitar el error 404 por pág desconocida con "get"
    produccionDisco = ProduccionDisco.objects.all()
    return render(request, "catalogo/disco.html", {'disco':disco,'produccionDisco':produccionDisco}) #Inyecta datos en página html
    #**************************

def banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id) #evitar el error 404 por pág desconocida con "get"
    musico = Musico.objects.all()
    integranteBanda = IntegranteBanda.objects.all()
    discos = Disco.objects.all().order_by('-fechaDisco','banda','titulo') #order by descendente para fecha y ascendente el resto
    return render(request, "catalogo/banda.html", {'banda':banda,'musico':musico,'integranteBanda':integranteBanda,'discos':discos}) #Inyecta datos en página html
    #**************************

def musico(request, musico_id):
    musico = get_object_or_404(Musico, id=musico_id) #evitar el error 404 por pág desconocida con "get"
    discos = Disco.objects.all().order_by('-fechaDisco') #order by descendente para fecha
    #produccionDisco = ProduccionDisco.objects.all().order_by('disco') #order by ascendentemente por disco
    #produccionDisco = ProduccionDisco.objects.filter(musico=musico_id) #selecciona con filtro de músico
    produccionDisco = ProduccionDisco.objects.all()
    #produccionDisco = ProduccionDisco.objects.all().select_related('disco').values_list('id','disco','musico','rol','descripcion','disco__fechaDisco','disco__titulo','disco__caratula','disco__banda').order_by('disco__fechaDisco')
    integranteBanda = IntegranteBanda.objects.all()
    return render(request, "catalogo/musico.html", {'musico':musico, 'produccionDisco':produccionDisco, 'integranteBanda':integranteBanda, 'discos':discos}) #Inyecta datos en página html
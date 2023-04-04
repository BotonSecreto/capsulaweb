from django.contrib import admin
from .models import Banda, Disco, Musico, ProduccionDisco, IntegranteBanda

class BandaAdmin(admin.ModelAdmin):
    #readonly_fields = ('nombre', 'descripBanda')
    list_display = ('nombreBanda',) #columnas expuestas
    ordering = ('nombreBanda',) #categorías ordenamiento 
    search_fields = ('nombreBanda','descripBanda') #para campo de busqueda
    #date_hierarchy = 'published' #navega por fechas
    list_filter = ('nombreBanda',) #filtro que permite agrupar por campos
    #pass
    
class MusicoAdmin(admin.ModelAdmin):
    #readonly_fields = ('nombreArt',')
    list_display = ('nombreArt',) #columnas expuestas incluye filtro de "listaBandas"
    ordering = ('nombreArt',) #categorías ordenamiento 
    search_fields = ('nombreArt',) #para campo de busqueda
    #date_hierarchy = 'published' #navega por fechas
    list_filter = ('nombreArt',) #filtro que permite agrupar por campos
    #pass
    
    #método para mostrar "lista de Bandas del Músico"
    #def listaBandas(self, obj):
    #    return ", ".join(
    #        [c.nombreBanda for c in obj.bandas.all().order_by("nombreBanda")])
    #listaBandas.short_description = "Bandas del Músico"

class DiscoAdmin(admin.ModelAdmin):
    #readonly_fields = ('titulo','fecha')
    list_display = ('titulo','fechaDisco','descripDisco','banda') #columnas expuestas incluye "listaColaboradores"
    ordering = ('fechaDisco','titulo','banda') #categorías ordenamiento 
    search_fields = ('titulo','descripBanda') #para campo de busqueda
    #date_hierarchy = 'published' #navega por fechas
    list_filter = ('titulo', 'banda','fechaDisco') #filtro que permite agrupar por campos
    #readonly_fields = ('created', 'updated')
    #pass

    #método para mostrar "lista de Bandas del Músico"
    #def listaColaboradores(self, obj):
    #    return ", ".join(
    #        [c.nombreArt for c in obj.musicos.all().order_by("nombreArt")])
    #listaColaboradores.short_description = "Colaboradores del Disco"

class ProduccionDiscoAdmin(admin.ModelAdmin):
    #readonly_fields = ('titulo','fecha')
    list_display = ('disco','musico','rol','descripcion') #columnas expuestas incluye "listaColaboradores"
    ordering = ('disco', ) #categorías ordenamiento 
    search_fields = ('disco','musico') #para campo de busqueda
    #date_hierarchy = 'published' #navega por fechas
    list_filter = ('disco', 'musico') #filtro que permite agrupar por campos
    #pass

    #método para mostrar "lista de Bandas del Músico"
    #def listaColaboradores(self, obj):
    #    return ", ".join(
    #        [c.nombreArt for c in obj.musico.all().order_by("nombreArt")])
    #listaColaboradores.short_description = "Colaboradores del Disco"

class IntegranteBandaAdmin(admin.ModelAdmin):
    #readonly_fields = ('titulo','fecha')
    list_display = ('banda','musico','rol','activo') #columnas expuestas incluye "listaColaboradores"
    ordering = ('banda', ) #categorías ordenamiento 
    search_fields = ('banda','musico') #para campo de busqueda
    #date_hierarchy = 'published' #navega por fechas
    list_filter = ('banda', 'musico') #filtro que permite agrupar por campos
    #pass

    #método para mostrar "lista de Bandas del Músico"
    #def listaIntegrantes(self, obj):
    #    return ", ".join(
    #        [c.nombreArt for c in obj.musico.all().order_by("nombreArt")])
    #listaIntegrantes.short_description = "Integrantes de la Banda"

admin.site.register(Banda, BandaAdmin)
admin.site.register(Musico, MusicoAdmin)
admin.site.register(Disco, DiscoAdmin)
admin.site.register(ProduccionDisco, ProduccionDiscoAdmin)
admin.site.register(IntegranteBanda, IntegranteBandaAdmin)


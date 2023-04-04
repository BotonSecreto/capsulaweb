from django.contrib import admin
from django.urls import path, include #importamos el "include"
from django.conf import settings #importa configuraciones para usar el modo DEBUG con imágenes
#*************
from django.conf import settings #importa configuraciones para usar el modo DEBUG con imágenes
urlpatterns = [
    path('', include('core.urls')), #IMPORTA TODAS LAS URL DEL "CORE"
    path('catalogo/', include('catalogo.urls')), #url formulario home, contiene el catálogo
    path('about/', include('about.urls')), #url sección "nosotros"
    path('contact/', include('contact.urls')), #url formulario contacto
    path('admin/', admin.site.urls),

]
if settings.DEBUG: #truco para fase de desarrollo que permite ver ARCHIVOS MEDIA en DEBUG
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

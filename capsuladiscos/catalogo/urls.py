from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name="catalogo"),
    #path('', views.disco, name="disco"),
    path('disco/<int:disco_id>/', views.disco, name="disco"),
    #path('disco/<int:disco_id>/banda/<int:banda_id>/', views.disco, name="disco"),
    path('banda/<int:banda_id>/', views.banda, name="banda"),
    path('musico/<int:musico_id>/', views.musico, name="musico"),
]
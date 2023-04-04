from django.db import models
from ckeditor.fields import RichTextField #importar app CKeditor
from django.utils.timezone import now
#from django.contrib.auth.models import User #importar clase User para usar atributos generales

class Banda(models.Model):
    nombreBanda = models.CharField(max_length=200,verbose_name="Nombre")
    imgBanda = models.ImageField(null=True, upload_to="bandas",verbose_name="Imagen Banda") #sube imágenes al directorio 'media/proyects'
    descripBanda = models.TextField(null=True, verbose_name="Descripción")
    link_sptf = models.URLField(null=True, blank=True,verbose_name="Link Spotify") #Crea el link del modelo
    link_apple = models.URLField(null=True, blank=True,verbose_name="Link Apple Music") #Crea el link del modelo
    link_ytb = models.URLField(null=True, blank=True,verbose_name="Link YouTube") #Crea el link del modelo
    link_ig = models.URLField(null=True, blank=True,verbose_name="Link Instagram") #Crea el link del modelo
    link_fb = models.URLField(null=True, blank=True,verbose_name="Link Facebook") #Crea el link del modelo
    link_tw = models.URLField(null=True, blank=True,verbose_name="Link Twitter") #Crea el link del modelo
    
    class Meta:
        verbose_name = "banda"
        verbose_name_plural = "bandas"

    def __str__(self):
        return self.nombreBanda

#********************************
class Musico(models.Model):
    nombreArt = models.CharField(max_length=200,verbose_name="Nombre Artístico")
    nombreReal = models.CharField(null=True, max_length=200,verbose_name="Nombre Real")
    imgMusico = models.ImageField(null=True, upload_to="musicos",verbose_name="Imagen Músico") #sube imágenes al directorio 'media/proyects'
    link_ig = models.URLField(null=True, blank=True,verbose_name="Link Instagram") #Crea el link del modelo
    link_fb = models.URLField(null=True, blank=True,verbose_name="Link Facebook") #Crea el link del modelo
    link_tw = models.URLField(null=True, blank=True,verbose_name="Link Twitter") #Crea el link del modelo
    #get_posts lo define para utilizar relación en ambos sentidos
   
    class Meta:
        verbose_name = "Músico"
        verbose_name_plural = "Músicos"

    def __str__(self):
        return self.nombreArt

#************************************
class Disco(models.Model):
    titulo = models.CharField(max_length=200,verbose_name="Título")
    caratula = models.ImageField(null=True, upload_to="catalogo",verbose_name="Carátula") #sube imágenes al directorio 'media/proyects'
    fechaDisco = models.DateField(default=now,verbose_name="Fecha de publicación")
    descripDisco = RichTextField(null=True, verbose_name="Descripción") #texto enriquecido formato con editor WYSIWYG
    link_sptf = models.TextField(null=True, max_length=500,verbose_name="Código inserción desde Spotify")
    link_apple = models.URLField(null=True, blank=True,verbose_name="Link Apple Music") #Crea el link del modelo
    link_ytb = models.URLField(null=True, blank=True,verbose_name="Link YouTube") #Crea el link del modelo
    link_tienda_cd = models.URLField(null=True, blank=True,verbose_name="Link Tienda Nacional CD") #Crea el link del modelo
    link_tienda_vin = models.URLField(null=True, blank=True,verbose_name="Link Tienda Nacional VINILO") #Crea el link del modelo
    link_tienda_cas = models.URLField(null=True, blank=True,verbose_name="Link Tienda Nacional CASSETTE") #Crea el link del modelo
    #campo relacione con tablas "Banda" y "Músicos"
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE,verbose_name="Banda")
    
    #ordenamiento por fecha de disco, banda y título en ese orden en MANTENEDOR
    ordering = ['-fechaDisco','banda','titulo'] 

    class Meta: #como se verá en el administrador
        verbose_name = "disco"
        verbose_name_plural = "discos"

    def __str__(self):
        return self.titulo

#*****************TABLAS DE UNIÓN "ProduccionDisco" Y "IntegranteBanda"
class ProduccionDisco(models.Model):
    #Información sobre Músicos participantes en la producción de cada disco.
    class Meta:
        order_with_respect_to = 'disco' #Músicos ordenados por Disco
        #ïndice único recomendable por si se accede desde el exterior de Django
        unique_together = [
            ('disco', 'musico'),
            ]
    #lISTA DE CONSTANTES, OPCIONES DE ROLES
    ROL_PRODUCCION = [
        (1, "Producción Musical"),
        (2, "Edición y Mezcla"),
        (3, "Masterización"),
        (4, "Músico invitado"),
        (5, "Otro"),
    ]
    #******* CAMPOS CLAVE
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE,verbose_name="Disco")
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE,verbose_name="Músico")
    #******* ATRIBUTOS
    rol = models.PositiveSmallIntegerField(verbose_name='Rol en la Producción',choices=ROL_PRODUCCION) 
    descripcion = models.TextField(null=True, verbose_name="Descripción de la colaboración")

class IntegranteBanda(models.Model):
    #Información sobre Músicos participantes en la producción de cada disco.
    class Meta:
        order_with_respect_to = 'banda' #Músicos ordenados por Disco
        #ïndice único recomendable por si se accede desde el exterior de Django
        unique_together = [
            ('banda', 'musico'),
            ]
    #lISTA DE CONSTANTES, OPCIONES DE ROLES
    ROL_BANDA = [
        (1, "Voz"),
        (2, "Bateria"),
        (3, "Bajo"),
        (4, "Guitarra"),
        (5, "Teclado/Piano"),
        (6, "Vientos"),
        (7, "Cuerdas"),
        (8, "Otro"),
    ]
    #******* CAMPOS CLAVE
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE,verbose_name="Banda")
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE,verbose_name="Músico")
    #******* ATRIBUTOS 
    rol = models.PositiveSmallIntegerField(verbose_name='Rol en la Banda',choices=ROL_BANDA) 
    activo = models.BooleanField(verbose_name="Activo actualmente", default=True)
#***************************

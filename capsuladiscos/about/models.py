from django.db import models
from ckeditor.fields import RichTextField #importar app CKeditor
# Create your models here.
#Cada clase representa una tabla con sus campos en la BD
class Nosotros(models.Model):
    #pass
    titulo = models.CharField(max_length=200,verbose_name="Título")
    #descripcion = models.TextField(verbose_name="Descripción")
    descripcion = RichTextField(verbose_name="Descripción") #texto enriquecido formato con editor WYSIWYG
    imagen = models.ImageField(upload_to="about",verbose_name="Imagen") #sube imágenes al directorio 'media/proyects'
    link = models.URLField(null=True, blank=True,verbose_name="Dirección Web") #Crea el link del modelo
    class Meta: #como se verá en el administrador
        verbose_name = "Nosotros"
        verbose_name_plural = "Nosotros"
    def __str__(self): 
        return self.titulo #que nombre mostrará en el administrador
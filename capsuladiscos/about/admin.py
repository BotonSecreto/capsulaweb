from django.contrib import admin

# Register your models here.
from .models import Nosotros
class NosotrosAdmin(admin.ModelAdmin):
    #readonly_fields = ('creado', 'actualizado') #deja como 'solo lectura' los campos para verlos en la plataforma
    pass
# Register your models here.
admin.site.register(Nosotros, NosotrosAdmin)
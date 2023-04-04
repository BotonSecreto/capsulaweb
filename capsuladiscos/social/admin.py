from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    #comprueba si usuario es de perfil "personal"
    def get_readonly_fields(self, request, obj):
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return()
admin.site.register(Link, LinkAdmin) 
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage #Importar para la estructura del correo
from .forms import ContactForm #Importamos el formulario
from capsuladiscos.settings import EMAIL_HOST_USER 

def contact(request):
    contact_form = ContactForm() #creamos una instancia en la vista

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "CápsulaDiscos.com: Nuevo mensaje de contacto", #ASUNTO
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content), #CUERPO
                EMAIL_HOST_USER, #EMAIL DE ORIGEN obtenido desde "email_setting.json"
                ["botonsecreto@gmail.com"], #EMAIL DE DESTINO DE TODOS LOS MENSAJES******
                reply_to=[email] #EMAIL DE RESPUESTA
            )
            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
        # else:
        #     return HttpResponse("Debe completar todos los campos del formulario")
    return render(request, "contact/contact.html",{'form':contact_form})

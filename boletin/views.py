# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
#import settings
from django.conf import settings
# import para envio de correo
from django.core.mail import send_mail

#Importar el modelo creado
from .models import Registrado

#Importar formularios a la vista
from .forms import RegModalForm,ContactForm
#importando el modelo base 
from .models import Registrado

# Create your views here.
#def home(request):
#     #si agregamos request.POST, le indicamos en el form q el metodo el POST y procesaremos la data como tal
#     #si se agrega el None, se desactivan los campos obligatorios
#     user_login = "Bienvenido Usuario logeado"
#     form = RegForm(request.POST or None)
#     #Operaciones que podemos ver o realizarle al form se pueden ver con print(dir(form)) en la terminal del servidor de djago
#     #print(dir(form))
#     if request.user.is_authenticated():
#         user_login = "Bienvenido %s"  %(request.user)

#     if form.is_valid():
#         # almacena toda la data del form en un diccionario usando el metodo cleaned_data
#         data_form = form.cleaned_data
#         #metodo get("nombre_campo_class_form") para traer el contenido
#         print data_form.get("nombre")
#         print data_form.get("email")
#         data_form_email = data_form.get("email")
#         #guardando en la BD Nombre_modelo_objects.metodo_create(nombres_campos_modelos = datos_procesados)
#         #obj_reg = Registrado.objects.create(email = data_form_email)

#         #Otra manera de guardar el objeto
#         # usar el nombre del modelo con su construsctor
#         data_obj = Registrado()
#         # obtener data para guardar en BD
#         data_obj.email = data_form.get("email")
#         data_obj.nombre = data_form.get("nombre")
#         # guardar el objeto en la bd
#         data_obj.save()

#     #limpiar el form
#     #form.clean_fields
#     context = { 
#         "form" : form,
#         "msj_user" : user_login
#      }
#     return render(request,'home.html',context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print form.cleaned_data
        email = form.cleaned_data.get("email")
        msj = form.cleaned_data.get("mensj")
        name = form.cleaned_data.get("nombre")

        # otra forma de sacar/mostrar/procesar data

        # print("iterando sobre la data almacenada y mostrandola")
        # for key,data in form.cleaned_data.iteritems():
        #     print key, data

        # print("otra forma mas sencilla de mostrar data almacenada")
        # for key in form.cleaned_data:
        #     print(key)
        #     print(form.cleaned_data.get(key))

        asunto = 'Envio de correo'
        mensj_email = "%s: %s enviado por %s" %(name, msj, email)
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, email]
        #send_mail
        send_mail(asunto,
            mensj_email,
            email_from,
            email_to,
            fail_silently = False
        )
        context = {
             "form" : form,
             "nombre" : name,
             "email" : email,
             "mensaje" : msj
         }
    
    error_data = "no almaceno correctamente"
    context = {
        "form" : form,
        "error_msj" : error_data
    }
    return render(request,"contact.html", context)

def home(request):
    
    context = {}
    return render(request, "base.html", context)
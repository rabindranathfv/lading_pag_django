# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#Importar el modelo creado
from .models import Registrado

#Importar formularios a la vista
from .forms import RegForm

# Create your views here.
def home(request):
    #si agregamos request.POST, le indicamos en el form q el metodo el POST y procesaremos la data como tal
    #si se agrega el None, se desactivan los campos obligatorios
    form = RegForm(request.POST or None)
    #Operaciones que podemos ver o realizarle al form se pueden ver con print(dir(form)) en la terminal del servidor de djago
    #print(dir(form))
    if form.is_valid():
        # almacena toda la data del form en un diccionario usando el metodo cleaned_data
        data_form = form.cleaned_data
        #metodo get("nombre_campo_class_form") para traer el contenido
        print data_form.get("nombre")
        print data_form.get("email")

    #limpiar el form
    #form.clean_fields
    context = { "form" : form }
    return render(request,'home.html',context)
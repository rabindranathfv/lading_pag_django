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
    context = { "form" : form }
    return render(request,'home.html',context)
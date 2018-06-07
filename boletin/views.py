# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#Importar el modelo creado
from .models import Registrado

#Importar formularios a la vista
from .forms import RegForm

# Create your views here.
def home(request):
    form = RegForm()
    context = { "form" : form }
    return render(request,'home.html',context)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#Importar el modelo creado
from .models import Registrado

# Create your views here.
def home(request):
    return render(request,'home.html',{})
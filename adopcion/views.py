# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Persona
# Create your views here.
from .forms import PersonaForm

def home(request):

    context = {}

    return render(request, "home.html",context)

def persona_add(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('adopcion:home')
    else:
        form = PersonaForm(request.POST or None)

    context = {'form': form}
    return render(request,"persona.html",context)
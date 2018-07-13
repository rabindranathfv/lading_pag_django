# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Centro
from .forms import CentroRefugioForm
## add for reverse url problem
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def centro_create_views(request):
    if request.method == 'POST':
        form = CentroRefugioForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('adopcion:home')
    else:
        form = CentroRefugioForm(request.POST or None)        
    context = {
        'form_ctxt': form
    }        
    return render(request,"centro.html",context)

def centro_list_views(request):
    print(Centro.objects.all())
    if request.method == 'GET':
        centro = Centro.objects.all()
    context = {
        'centro_ctxt': centro
    }
    return render(request,"centro_list.html",context)

def centro_edit_views(request,centro_id):
    centro = Centro.objects.get(pk=centro_id)
    if request.method == 'GET':
        # captura el evento get y guarda la instacia en el model correspondiente
        form = CentroRefugioForm(instance = centro)
    else:
        if request.method == 'POST':
            form = CentroRefugioForm(request.POST or None,instance = centro)
            if form.is_valid():
                form.save()
            return redirect('centro:listar-centro')
    context = {
        'form_ctxt': form
    }
    return render(request,"centro.html",context)

    
def centro_delete_views(request,centro_id):
    centro = Centro.objects.get(pk = centro_id)
    if request.method == 'POST':
        centro.delete()
        return redirect('centro:listar-centro')
    context = {
        'centro_ctxt': centro
    }
    return render(request,"centro_list.html",context)
    
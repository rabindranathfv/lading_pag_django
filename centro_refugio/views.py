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
        'form': form
    }        
    return render(request,"refugio.html",context)

def centro_list_views(request):
    print(Centro.objects.all())
    if request.method == 'GET':
        centro = Centro.objects.all()
    context = {
        'centro': centro
    }
    return render(request,"centro_list.html",context)
    #return HttpResponseRedirect(reverse('centro_refugio:listar'))

def centro_edit_views(request,id_refugio):
    centro = Centro.objects.get(pk=id_refugio)
    if request.method == 'GET':
        # captura el evento get y guarda la instacia en el model correspondiente
        form = CentroRefugioForm(instance = centro)
    else:
        if request.method == 'POST':
            form = CentroRefugioForm(request,instance = centro)
            if form.is_valid():
                form.save()
            return redirect('centro_Refugio:centro_list_views')
    context = {
        'form': form
    }
    return render(request,"refugio.html",context)

    
def centro_delete_views(request,id_refugio):
    centro = Centro.objects.get(pk = id_refugio)
    if request.method == 'POST':
        centro.delete()
        return redirect('centro_refugio:centro_list_views')
    context = {
        'centro': centro
    }
    return render(request,"centro_list.html",context)
    
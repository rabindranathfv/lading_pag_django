# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Vacuna,Mascota
from .forms import MascotaForm

# Create your views here.
def mascota_views(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MascotaForm(request.POST or None)

    context = {'form': form}
    return render(request,"mascota.html",context)

def mascota_list_views(request):
    # QuerySet for list pets
    mascota = Mascota.objects.all()
    print(mascota)
    context = {
        'mascotas': mascota,
    }
    return render(request,"mascota_list.html",context)

def mascota_edit_views(request,mascota_id):
    mascota = Mascota.objects.get(pk=mascota_id)
    
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        if request.method == 'POST':
            form = MascotaForm(request.POST,instance=mascota)
            if form.is_valid():
                form.save()
            return redirect('mascota:listar-mascotas')
    return render(request,"mascota.html",context= { 'form': form})

def mascota_delete_views(request,mascota_id):
    mascota = Mascota.objects.get(pk=mascota_id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:listar-mascotas')
    return render(request, "mascota_delete.html",context={ 'mascotas': mascota})
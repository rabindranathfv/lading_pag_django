# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Vacuna,Mascota
from .forms import MascotaForm

# Create your views here.
def mascota_views(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = MascotaForm(request.POST or None)

    context = {'form': form}
    return render(request,"mascota.html",context)
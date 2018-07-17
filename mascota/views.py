# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Vacuna,Mascota
from .forms import MascotaForm

# for xhtml2pdf
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template


# Create your views here.
def mascota_views(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('mascota:mascota')
    else:
        form = MascotaForm(request.POST or None)

    context = {'form': form}
    return render(request,"mascota.html",context)

def mascota_list_views(request):
    # QuerySet for list pets
    mascota = Mascota.objects.all()
    print mascota 
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

# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         #obtener el template
#         template = get_template('pdf/mascota_pdf.html')
#         # queryset
#         mascota = Mascota.objects.all()
#         # Data a renderizar en el template
#         context = {
#             'mascotas' : mascota,
#         }
#         # render template
#         html = template.render(context)
#         #respuesta del pdf en el navegador
#         return HttpResponse(html)

def GeneratePDF(request,*args , **kwargs):
    #obtener el template
    template = get_template('pdf/mascota_pdf.html')
    # queryset
    mascota = Mascota.objects.all()
    # Data a renderizar en el template
    context = {
        'mascotas' : mascota,
    }
    # render template
    html = template.render(context)
    # to download in pdf
    pdf = render_to_pdf('pdf/mascota_pdf.html',context)
    #respuesta del pdf en el navegador
    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponse("Crear pagina de Error 404")
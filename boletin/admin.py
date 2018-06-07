# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# namespace.models import nombre_modelo
from .models import Registrado

class RegistradoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email","timestamp")
# registrado el modelo Registrado dentro del admin
admin.site.register(Registrado,RegistradoAdmin)
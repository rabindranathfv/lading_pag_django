# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# namespace.models import nombre_modelo
from .models import Registrado

# registrado el modelo Registrado dentro del admin
admin.site.register(Registrado)
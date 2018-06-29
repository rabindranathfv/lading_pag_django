# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Vacuna,Mascota

# Register your models here.
admin.site.register(Vacuna,Mascota)
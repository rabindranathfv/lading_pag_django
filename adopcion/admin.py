# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# import models for register in admin
from adopcion.models import Persona

# Register your models here.
admin.site.register(Persona)
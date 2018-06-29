# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Centro(models.Model):
    
    nombre_centro = models.CharField(max_length=255)
    visita = models.ForeignKey('adopcion.Persona', on_delete=models.CASCADE)
    mascota = models.OneToOneField('mascota.Mascota',blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre_centro

    def __unicode__(self):
        return self.nombre_centro


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre
        


class Mascota(models.Model):
    
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey('adopcion.Persona',blank=True, null=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna,blank=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)
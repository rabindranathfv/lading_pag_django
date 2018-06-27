# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# add for use User model from django
from django.contrib.auth.models import User # User model por defecto de django
from django.db.models.signals import post_save # Control para guardar autenticacion

import uuid
# Create your models here.

def User_account(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE) # hacemos erferencia hacia User y heredamos todos sus atributos mas los que adicionaremos

    #Custom fields
    company_name = models.CharField(max_length = 255, blank = True)


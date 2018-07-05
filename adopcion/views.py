# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Persona
# Create your views here.

def home(request):

    context = {}

    return render(request, "home.html",context)
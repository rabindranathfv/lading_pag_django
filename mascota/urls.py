"""web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

#import para la config de los ambientes si el debug es true
from django.conf import settings
from django.conf.urls.static import static

#from .views import GeneratePDF,mascota_views,mascota_list_views,mascota_edit_views,mascota_delete_views
from . import views

urlpatterns = [
    url(r'^agregar_mascota/$', views.mascota_views,name="mascota"),
    url(r'^listar/$', views.mascota_list_views,name="listar-mascotas"),
    url(r'^editar/(?P<mascota_id>[0-9]+)/$', views.mascota_edit_views,name="editar-mascota"),
    url(r'^eliminar/(?P<mascota_id>[0-9]+)/$', views.mascota_delete_views,name="eliminar-mascota"),

    # generacion de pdf
    # funciona con la vista basada en clases
    #url(r'^pdf/$', GeneratePDF.as_view()),
    # vista basada en funciones
    url(r'^pdf/$', views.GeneratePDF),
]
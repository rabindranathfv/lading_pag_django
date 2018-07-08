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

from . import views

urlpatterns = [
    url(r'^refugio/$', views.centro_create_views, name='crear-refugio'),
    url(r'^refugio/editar/?P<id_refugio>[0-9]+/$', views.centro_edit_views, name='editar-refugio'),
    url(r'^refugio/eliminar/?P<id_refugio>[0-9]+/$', views.centro_delete_views, name='eliminar-refugio'),  
    #url(r'^refugio/listar/$', views.centro_list_views, name='lista de refugios'),
    url(r'^refugio/listar/$', views.centro_list_views, name='listar-refugios'),
]
from django.conf.urls import patterns, include, url
from . import views

urlpatterns =[

	url(r'^$' , 'mensaje.views.buzon_entrada', name='buzon_entrada'),

    url(r'^crear/' , 'mensaje.views.mensaje_crear', name='mensaje_crear'),


]
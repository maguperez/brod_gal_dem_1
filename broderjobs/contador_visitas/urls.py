from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^oportunidad-enviar/$', 'contador_visitas.views.oportunidad_enviar', name="contador-visitas-oportunidad-enviar"),

    url(r'^oportunidad-obtener/$', 'contador_visitas.views.oportunidad_obtener', name="contador-visitas-oportunidad-obtener"),
]


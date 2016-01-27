from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^formulario-estudiante/$', 'disc.views.formulario_estudiante', name="disc-formulario-estudiante"),
    url(r'^preguntas-estudiante/$', 'disc.views.preguntas_estudiante', name="disc-preguntas-estudiante"),
    url(r'^respuesta-estudiante/$', 'disc.views.respuesta_estudiante', name="disc-respuesta-estudiante"),
    url(r'^finalizo-estudiante/$', 'disc.views.finalizo_estudiante', name="disc-finalizo-estudiante"),
]
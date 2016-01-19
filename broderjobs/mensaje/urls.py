from django.conf.urls import patterns, include, url
from . import views

urlpatterns =[

	url(r'^$' , 'mensaje.views.buzon_entrada', name='buzon_entrada'),

    url(r'^crear/' , 'mensaje.views.mensaje_crear', name='mensaje_crear'),

    url(r'^ver/', 'mensaje.views.mensaje_ver', name='mensaje-ver'),

    url(r'^enviar-estudiante/', 'mensaje.views.mensaje_enviar_estudiantes', name='mensaje-enviar-estudiante'),

    url(r'^enviar/', 'mensaje.views.mensaje_enviar', name='mensaje-enviar'),

    url(r'^notificacion-vistas/', 'mensaje.views.mensaje_notificacion_vista', name='mensaje-notificacion-vistas'),

    url(r'^listar/', views.MensajeBuscarView.as_view(), name='mensaje-buscar'),

    url(r'^abrir-con-relacionados/', views.MensajeAbrirConRelacionados.as_view(), name='mensaje-abrir-con-relacionados'),

]
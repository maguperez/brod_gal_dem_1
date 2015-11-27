from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^crear/', views.OportunidadCrearView.as_view(), name='oportunidad_crear'),
    url(r'^editar/(?P<id>\d+)/', views.OportunidadEditarView.as_view(), name='oportunidad-editar'),
    # url(r'^postular/(?P<id>\d+)/', views.PostularView.as_view(), name='oportunidad-postular'),
]

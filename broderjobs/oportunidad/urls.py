from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^crear/', views.OportunidadCrearView.as_view(), name='oportunidad_crear'),
]

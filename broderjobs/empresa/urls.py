from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^oportunidad-listar/', views.OportunidadListarView.as_view(), name='empresa-oportunidad-listar'),

    url(r'^oportunidad-busqueda/$', views.OportunidadBusquedaView.as_view(), name="empresa-oportunidad-busqueda"),

    url(r'^configuracion/$', views.ConfiguracionView.as_view(), name="empresa-configuracion"),

    url(r'^mi-empresa/$', views.MiEmpresaView.as_view(), name="mi-empresa"),

    url(r'^mi-empresa/info-general/$', views.InfoGeneralView.as_view(), name="mi-empresa-info-general"),

    url(r'^mi-empresa/logo/$', views.LogoView.as_view(), name="mi-empresa-logo"),



]

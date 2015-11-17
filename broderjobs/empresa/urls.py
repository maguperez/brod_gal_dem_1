from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^oportunidad-listar/', 'empresa.views.oportunidad_listar', name='empresa_oportunidad_listar'),

    url(r'^mi-empresa/$', views.MiEmpresaView.as_view(), name="mi_empresa"),

    url(r'^mi-empresa/info-general/$', views.InfoGeneralView.as_view(), name="mi_empresa_info_general"),

    url(r'^mi-empresa/logo/$', views.LogoView.as_view(), name="mi_empresa_logo"),
]

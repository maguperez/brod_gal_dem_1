from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    # url(r'^oportunidad-listar/', views.OportunidadListarView.as_view(), name='empresa-oportunidad-listar'),
    # url(r'^oportunidad-listar/', 'empresa.views.oportunidad_listar', name='empresa-oportunidad-listar'),

    # url(r'^oportunidad-busqueda/$', views.OportunidadBusquedaView.as_view(), name="empresa-oportunidad-busqueda"),

    # url(r'^oportunidad-detalle/(?P<id>\d+)/$', views.OportunidadDetalleView.as_view(), name="empresa-oportunidad-detalle"),

    url(r'^mi-empresa/$', views.MiEmpresaView.as_view(), name="mi-empresa"),

    url(r'^mi-empresa/info-general/$', views.InfoGeneralView.as_view(), name="mi-empresa-info-general"),

    url(r'^mi-empresa/logo/$', views.LogoView.as_view(), name="mi-empresa-logo"),

    url(r'^mi-empresa/ubicacion/$', views.UbicacionView.as_view(), name="mi-empresa-ubicacion"),

    url(r'^oportunidades/', 'empresa.views.oportunidades', name='empresa-oportunidad-lista'),

    url(r'^oportunidad-listar/', 'empresa.views.oportunidades_listar', name='empresa-oportunidad-listar'),

    url(r'^oportunidad-busqueda/$', 'empresa.views.oportunidad_busqueda', name="empresa-oportunidad-busqueda"),

    url(r'^oportunidad-postulaciones/$', views.OportunidadPostulacionesView.as_view(), name="empresa-oportunidad-postulaciones"),

    url(r'^oportunidad-estudiantes/$', views.OportunidadEstudiantes.as_view(), name="empresa-oportunidad-estudiantes"),

]

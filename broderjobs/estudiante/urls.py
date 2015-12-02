from django.conf.urls import patterns, include, url
from . import views


urlpatterns = [
	url(r'^registro-cv/', 'estudiante.views.registro_cv', name='registro-cv'),

	url(r'^oportunidad-listar/', 'estudiante.views.oportunidad_listar', name='estudiante-oportunidad-listar'),

	url(r'^mi-cv/resumen/$', views.ResumenView.as_view(), name="mi-cv-resumen"),

	url(r'^mi-cv/foto/$', views.FotoView.as_view(), name="mi-cv-foto"),

	url(r'^mi-cv/info-personal/$', views.InfoPersonalView.as_view(), name="mi-cv-info-personal"),

	url(r'^mi-cv/disponibilidad/$', views.DisponibilidadView.as_view(), name="mi-cv-disponibilidad"),

	url(r'^mi-cv/idioma/$', views.IdiomaView.as_view(), name="mi-cv-idioma"),

	url(r'^mi-cv/conocimiento/$', views.ConocimientoView.as_view(), name="mi-cv-conocimiento"),
	
	url(r'^mi-cv/actividad-extra/(?P<id>\d+)/$', views.ActividadExtraView.as_view(), name="mi-cv-actividad-extra-editar"),

	url(r'^mi-cv/actividad-extra-crear/$', views.ActividadExtraCrearView.as_view(), name="mi-cv-actividad-extra-crear"),

	url(r'^mi-cv/actividad-extra-eliminar/(?P<pk>\d+)/$', views.ActividadExtraEliminarView.as_view(), name="mi-cv-actividad-extra-eliminar"),

	url(r'^mi-cv/experiencia/(?P<id>\d+)/$', views.ExperienciaView.as_view(), name="mi-cv-experiencia-editar"),

	url(r'^mi-cv/experiencia/$', views.ExperienciaView.as_view(), name="mi-cv-experiencia-editar"),

	url(r'^mi-cv/experiencia-crear/$', views.ExperienciaCrearView.as_view(), name="mi-cv-experiencia-crear"),

	url(r'^mi-cv/experiencia-eliminar/(?P<pk>\d+)/$', views.ExperienciaEliminarView.as_view(), name="mi-cv-experiencia-eliminar"),

	url(r'^mi-cv/voluntariado/(?P<id>\d+)/$', views.VoluntariadoView.as_view(), name="mi-cv-voluntariado-editar"),

	url(r'^mi-cv/voluntariado-crear/$', views.VoluntariadoCrearView.as_view(), name="mi-cv-voluntariado-crear"),

	url(r'^mi-cv/voluntariado-eliminar/(?P<pk>\d+)/$', views.VoluntariadoEliminarView.as_view(), name="mi-cv-voluntariado-eliminar"),

	url(r'^mi-cv/$', views.MiCVView.as_view(), name="mi-cv"),

	url(r'^empresa-lista/$', views.EmpresaListaView.as_view(), name="estudiante-empresa-lista"),

	url(r'^empresa-busqueda/$', views.EmpresaBusquedaView.as_view(), name="estudiante-empresa-busqueda"),

	url(r'^empresa-detalle/(?P<id>\d+)/$', views.EmpresaDetalleView.as_view(), name="estudiante_empresa_detalle"),

	url(r'^universidad-busqueda/$', views.UniversidadBusquedaView.as_view(), name="universidad-busqueda"),

	url(r'^carrera-busqueda/$', views.CarreraBusquedaView.as_view(), name="carrera-busqueda"),

	url(r'^pais-busqueda/$', views.PaisBusquedaView.as_view(), name="pais-busqueda"),

	url(r'^ciudad-busqueda/$', views.CiudadBusquedaView.as_view(), name="ciudad-busqueda"),

	url(r'^estudiante-empresa-busqueda/$', views.EstudianteEmpresaBusquedaView.as_view(), name="empresa-busqueda"),

	url(r'^estudiante-puesto-busqueda/$', views.EstudiantePuestoBusquedaView.as_view(), name="puesto-busqueda"),

	url(r'^oportunidad-busqueda/$', views.OportunidadBusquedaView.as_view(), name="estudiante-oportunidad-busqueda"),

	url(r'^oportunidad-detalle/(?P<id>\d+)/$', views.OportunidadDetalleView.as_view(), name="estudiante-oportunidad-detalle"),

	url(r'^oportunidad-postular/$', views.OportunidadPostularView.as_view(), name="estudiante-oportunidad-postular"),

	url(r'^mis-procesos/$', views.ProcesosView.as_view(), name="estudiante-procesos"),

]

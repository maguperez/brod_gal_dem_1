from django.conf.urls import patterns, include, url
from . import views


urlpatterns =[

	url(r'^registro-cv/', 'estudiante.views.registro_cv', name='registro-cv'),

	url(r'^oportunidad-listar/', 'estudiante.views.oportunidad_listar', name='oportunidad-listar'),

	url(r'^configuracion/$', views.ConfiguracionView.as_view(), name="estudiante-configuracion"),

	url(r'^editar-cuenta/$', views.EditarCuentaView.as_view(), name="estudiante-editar-cuenta"),

	url(r'^mi-cv/resumen/$', views.ResumenView.as_view(), name="mi-cv-resumen"),

	url(r'^mi-cv/foto/$', views.FotoView.as_view(), name="mi-cv-foto"),

	url(r'^mi-cv/info-personal/$', views.InfoPersonalView.as_view(), name="mi-cv-info-personal"),

	url(r'^mi-cv/disponibilidad/$', views.DisponibilidadView.as_view(), name="mi-cv-disponibilidad"),

	url(r'^mi-cv/idioma/$', views.IdiomaView.as_view(), name="mi-cv-idioma"),

	url(r'^mi-cv/conocimiento/$', views.ConocimientoView.as_view(), name="mi-cv-conocimiento"),

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

	url(r'^empresa-detalle/(?P<id>\d+)/$', views.EmpresaDetalleView.as_view(), name="estudiante-empresa-detalle"),
]

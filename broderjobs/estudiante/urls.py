from django.conf.urls import patterns, include, url
from . import views


urlpatterns =[

	url(r'^registro-cv/', 'estudiante.views.registro_cv', name='registro_cv'),

	url(r'^oportunidad-listar/', 'estudiante.views.oportunidad_listar', name='oportunidad_listar'),

	#url(r'^mi-cv/$', 'estudiante.views.mi_cv', name='mi_cv'),

	url(r'^mi-cv/resumen/$', views.ResumenView.as_view(), name="mi_cv_resumen"),

	url(r'^mi-cv/foto/$', views.FotoView.as_view(), name="mi_cv_foto"),

	url(r'^mi-cv/info-personal/$', views.InfoPersonalView.as_view(), name="mi_cv_info_personal"),

	url(r'^mi-cv/disponibilidad/$', views.DisponibilidadView.as_view(), name="mi_cv_disponibilidad"),

	url(r'^mi-cv/idioma/$', views.IdiomaView.as_view(), name="mi_cv_idioma"),

	url(r'^mi-cv/conocimiento/$', views.ConocimientoView.as_view(), name="mi_cv_conocimiento"),

	url(r'^mi-cv/experiencia/(?P<id>\d+)/$', views.ExperienciaView.as_view(), name="mi_cv_experiencia_editar"),

	url(r'^mi-cv/experiencia-crear/$', views.ExperienciaCrearView.as_view(), name="mi_cv_experiencia_crear"),

	url(r'^mi-cv/experiencia-eliminar/(?P<id>\d+)/$', views.ExperienciaEliminarView.as_view(), name="mi_cv_experiencia_eliminar"),
	
	url(r'^mi-cv/voluntariado/(?P<id>\d+)/$', views.VoluntariadoView.as_view(), name="mi_cv_voluntariado_editar"),

	url(r'^mi-cv/voluntariado-crear/$', views.VoluntariadoCrearView.as_view(), name="mi_cv_voluntariado_crear"),

	url(r'^mi-cv/voluntariado-eliminar/(?P<id>\d+)/$', views.VoluntariadoEliminarView.as_view(), name="mi_cv_voluntariado_eliminar"),

	url(r'^mi-cv/$', views.MiCVView.as_view(), name="mi_cv"),
]

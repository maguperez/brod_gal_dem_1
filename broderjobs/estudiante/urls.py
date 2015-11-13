from django.conf.urls import patterns, include, url
from . import views


urlpatterns =[

	url(r'^registro-cv/', 'estudiante.views.registro_cv', name='registro_cv'),

	url(r'^oportunidad-listar/', 'estudiante.views.oportunidad_listar', name='oportunidad_listar'),

	#url(r'^mi-cv/$', 'estudiante.views.mi_cv', name='mi_cv'),

	url(r'^mi-cv-info-personal/$' , 'estudiante.views.info_personal', name='info_personal'),

	url(r'^mi-cv/resumen/$', views.ResumenView.as_view(), name="mi_cv_resumen"),

	url(r'^mi-cv/$', views.MiCVView.as_view(), name="mi_cv"),
]

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^registro-cv/', 'estudiante.views.registro_cv', name='registro_cv'),
	url(r'^oportunidad-listar/', 'estudiante.views.oportunidad_listar', name='oportunidad_listar'),

)

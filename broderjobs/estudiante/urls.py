from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^registro/', 'estudiante.views.RegistroCV', name='registrocv')

)

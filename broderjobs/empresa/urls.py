from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^oportunidad-listar/', 'empresa.views.oportunidad_listar', name='empresa_oportunidad_listar'),
                       )

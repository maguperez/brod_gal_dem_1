from django.conf.urls import patterns, include, url
from . import views



urlpatterns =[

	url(r'^$' , 'main.views.homepage', name='homepage'),

	url(r'^estudiante/$' , 'main.views.estudiante', name='estudiante'),

	url(r'^empresa/$' , 'main.views.homepage_empresa', name='empresa'),

	url(r'^estudiante-login/$' , 'main.views.login_estudiante', name='estudiante-login'),

	url(r'^empresa-login/$' , 'main.views.empresa_login', name='empresa-login'),

	url(r'^salir/$' , 'django.contrib.auth.views.logout_then_login', name='salir'),

	url(r'^estudiante-registro/$','main.views.estudiante_registro' , name = 'estudiante-registro'),

	url(r'^empresa-registro/$','main.views.empresa_registro' , name = 'empresa-registro'),

	url(r'^configuracion/$', views.ConfiguracionView.as_view(), name="configuracion"),

	url(r'^editar-cuenta/$', views.EditarCuentaView.as_view(), name="editar-cuenta"),

]
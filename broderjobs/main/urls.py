from django.conf.urls import patterns, include, url
from .views import EstudianteResgistro, EmpresaRegistro


urlpatterns = patterns('',

	url(r'^$' , 'main.views.homepage', name='homepage'),

	url(r'^estudiante/$' , 'main.views.estudiante', name='estudiante'),

	url(r'^empresa/$' , 'main.views.empresa', name='empresa'),

	url(r'^estudiante-login/$' , 'main.views.login_page', name='login'),

	url(r'^empresa-login/$' , 'main.views.empresa_login', name='empresa-login'),

	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
		 name='logout'),

	#url(r'^estudiante_registro/$', EstudianteResgistro.as_view() , name = 'estudiante_registro'),
	url(r'^estudiante-registro/$','main.views.register_user' , name = 'estudiante-registro'),

	url(r'^empresa-registro/$', EmpresaRegistro.as_view() , name = 'empresa-registro')
		#url(r'^logout/$' , 'main.views.logout', name='logout'),

	#url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
	#	 name='logout'),

	#url(r'^estudiante_login/$' , 'django.contrib.auth.views.login',
	#	{'template_name':'main/estudiante-login.html'}, name='login'),

)

from django.conf.urls import patterns, include, url
from . import views



urlpatterns =[

	url(r'^$' , 'main.views.homepage', name='homepage'),

	url(r'^estudiante/$' , 'main.views.homepage', name='estudiante'),

	# url(r'^estudiante/$' , 'main.views.estudiante', name='estudiante'),

	url(r'^empresa/$' , 'main.views.homepage_empresa', name='empresa'),

	# url(r'^empresa/$' , 'main.views.empresa', name='empresa'),
    #
	# url(r'^estudiante-login/$' , 'main.views.login_estudiante', name='estudiante-login'),
    #
	# url(r'^empresa-login/$' , 'main.views.empresa_login', name='empresa-login'),

	url(r'^salir/$' , 'django.contrib.auth.views.logout_then_login', name='salir'),

	# url(r'^estudiante-registro/$','main.views.estudiante_registro' , name = 'estudiante-registro'),

	# url(r'^empresa-registro/$','main.views.empresa_registro' , name = 'empresa-registro'),

	url(r'^usuarios/$', views.UsuariosView.as_view(), name="usuarios"),

	url(r'^editar-cuenta/$', 'main.views.editar_cuenta', name="editar-cuenta"),

	url(r'^terminos-condiciones/$', 'main.views.terminos_condiciones', name="terminos-condiciones"),

	url(r'^404/$', 'main.views.error404', name="404"),

	# url(r'^editar-cuenta-representante/$', 'main.views.editar_cuenta_representante', name="editar-cuenta-representante"),

	# url(r'^editar-cuenta/$', views.EditarUsuarioEstudianteView.as_view(), name="editar-cuenta"),

	url(r'^pais-busqueda/$', views.PaisBusquedaView.as_view(), name="pais-busqueda"),

	url(r'^ciudad-busqueda/$', views.CiudadBusquedaView.as_view(), name="ciudad-busqueda"),

	url(r'^carrera-busqueda/$', views.CarreraBusquedaView.as_view(), name="ciudad-busqueda"),

]
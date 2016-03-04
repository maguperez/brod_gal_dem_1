from django.conf.urls import patterns, include, url
from . import views



urlpatterns =[

	url(r'^$' , 'main.views.homepage', name='homepage'),

	url(r'^estudiante/$' , 'main.views.homepage', name='estudiante'),

	url(r'^empresa/$' , 'main.views.homepage_empresa', name='empresa'),

	url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),
	url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),

	url(r'^salir/$' , 'django.contrib.auth.views.logout_then_login', name='salir'),

	url(r'^usuarios/$', views.UsuariosView.as_view(), name="usuarios"),

	url(r'^cuenta-editar/$', views.CuentaEditarView.as_view(), name="cuenta-editar"),

	url(r'^contrasena-editar/$', 'main.views.contrasena_editar', name="contrasena-editar"),

	url(r'^terminos-condiciones/$', 'main.views.terminos_condiciones', name="terminos-condiciones"),

	url(r'^404/$', 'main.views.error404', name="404"),

	# url(r'^editar-cuenta-representante/$', 'main.views.editar_cuenta_representante', name="editar-cuenta-representante"),

	# url(r'^editar-cuenta/$', views.EditarUsuarioEstudianteView.as_view(), name="editar-cuenta"),

	url(r'^universidad-busqueda/$', views.UniversidadBusquedaView.as_view(), name="universidad-busqueda"),

	url(r'^pais-busqueda/$', views.PaisBusquedaView.as_view(), name="pais-busqueda"),

	url(r'^ciudad-busqueda/$', views.CiudadBusquedaView.as_view(), name="ciudad-busqueda"),

	url(r'^carrera-busqueda/$', views.CarreraBusquedaView.as_view(), name="carrera-busqueda"),

	url(r'^carrera-busqueda-por-tipo/$', views.CarreraBusquedaPorTipoView.as_view(), name="carrera-busqueda-por-tipo"),

	url(r'^periodos-graduacion-busqueda/$', views.PeriodosGraduacionBusquedaView.as_view(), name="periodos-graduacion-busqueda"),

]
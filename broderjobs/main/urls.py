from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth import views as auth_views



urlpatterns =[

	url(r'^$' , 'main.views.homepage', name='homepage'),

	url(r'^estudiante/$' , 'main.views.homepage', name='estudiante'),

	url(r'^empresa/$' , 'main.views.homepage_empresa', name='empresa'),

	url(r'^salir/$' , 'django.contrib.auth.views.logout_then_login', name='salir'),

	url(r'^usuarios/$', views.UsuariosView.as_view(), name="usuarios"),

	url(r'^cuenta-editar/$', views.CuentaEditarView.as_view(), name="cuenta-editar"),

	url(r'^cuenta-crear/$', views.CuentaCrearView.as_view(), name="cuenta-crear"),

	url(r'^contrasena-editar/$', 'main.views.contrasena_editar', name="contrasena-editar"),

	# url(r'^contrasena-crear/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
	# 	auth_views.password_reset_confirm, {'template_name': 'main/contrasena-crear.html'}, name="contrasena-crear"),

	url(r'^contrasena-crear/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.password_reset_confirm, {'template_name': 'main/contrasena-restablecer.html',
										'post_reset_redirect' : 'homepage'}, name="contrasena-crear"),

	url(r'^contrasena-recuperar/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.password_reset_confirm, {'template_name': 'main/contrasena-restablecer.html',
										'post_reset_redirect' : 'homepage'}, name="contrasena-recuperar"),

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


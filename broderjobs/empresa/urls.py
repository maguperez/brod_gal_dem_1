from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    # url(r'^oportunidad-listar/', views.OportunidadListarView.as_view(), name='empresa-oportunidad-listar'),
    # url(r'^oportunidad-listar/', 'empresa.views.oportunidad_listar', name='empresa-oportunidad-listar'),

    # url(r'^oportunidad-busqueda/$', views.OportunidadBusquedaView.as_view(), name="empresa-oportunidad-busqueda"),

    # url(r'^oportunidad-detalle/(?P<id>\d+)/$', views.OportunidadDetalleView.as_view(), name="empresa-oportunidad-detalle"),

    url(r'^mi-empresa/$', views.MiEmpresaView.as_view(), name="mi-empresa"),

    url(r'^mi-empresa/info-general/$', views.InfoGeneralView.as_view(), name="mi-empresa-info-general"),

    url(r'^mi-empresa/logo/$', views.LogoView.as_view(), name="mi-empresa-logo"),

    url(r'^mi-empresa/ubicacion/$', views.UbicacionView.as_view(), name="mi-empresa-ubicacion"),

    url(r'^mi-empresa/redes-sociales/$', views.RedesSocialesView.as_view(), name="mi-empresa-redes-sociales"),

    url(r'^oportunidades/', 'empresa.views.oportunidades', name='empresa-oportunidad-lista'),

    url(r'^oportunidad-listar/', 'empresa.views.oportunidades_listar', name='empresa-oportunidad-listar'),

    url(r'^oportunidad-busqueda/$', 'empresa.views.oportunidad_busqueda', name="empresa-oportunidad-busqueda"),

    url(r'^oportunidad-cargar-lista/$', 'empresa.views.oportunidad_cargar_lista', name="empresa-oportunidad-cargar-lista"),

    url(r'^oportunidad-buscar/$', views.OportunidadBuscarView.as_view(), name="empresa-oportunidad-buscar"),

    url(r'^oportunidad-postulaciones/$', views.OportunidadPostulacionesView.as_view(), name="empresa-oportunidad-postulaciones"),

    url(r'^oportunidad-estudiantes/$', views.OportunidadEstudiantes.as_view(), name="empresa-oportunidad-estudiantes"),

    url(r'^oportunidad-candidatos/(?P<id>\d+)/$', views.OportunidadCandidatos.as_view(), name="empresa-oportunidad-candidatos"),

    url(r'^oportunidad-candidatos/(?P<id>\d+)/cv/(?P<e>\d+)$', views.OportunidadCandidatosCV.as_view(), name="empresa-oportunidad-candidatos-cv"),

    url(r'^candidato-cv-pdf/$', 'empresa.views.canditado_cv_pdf', name="empresa-candidato-cv-pdf"),

    url(r'^mi-empresa/slider-imagenes/(?P<id>\d+)/$', 'empresa.views.empresa_slider_imagenes', name="empresa-slider-imagenes"),
    url(r'^mi-empresa/delete/(?P<pk>\d+)$', views.PictureDeleteView.as_view(), name='upload-delete'),
    url(r'^mi-empresa/imagenes/$', views.PictureCreateView.as_view(), name='upload-new'),
    url(r'^mi-empresa/imagenes/view/$', views.PictureListView.as_view(), name='upload-view'),

    url(r'^mi-empresa/video-delete/$', 'empresa.views.video_url_delete', name='empresa-video-delete'),
    url(r'^mi-empresa/video-create/$','empresa.views.video_url_create', name='empresa-video-create'),
    url(r'^mi-empresa/video-list/view/$', 'empresa.views.video_url_list', name='empresa-video-list'),
    url(r'^mi-empresa/videos/$', views.VideosListView.as_view(), name='videos-list'),

    url(r'^prueba/$','empresa.views.prueba', name='prueba'),
    url(r'^prueba_empresa/$','empresa.views.prueba_empresa', name='prueba_empresa'),

    url(r'^empresa-busqueda/$', views.EmpresaBusquedaView.as_view(), name="empresa-busqueda"),

]

handler404 = 'app.views.404_view'
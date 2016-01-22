from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from app.views import error

urlpatterns = [
    #INICIO ESTUDIANTES
    url(r'^', include('main.urls')),

    url(r'^estudiante/', include('estudiante.urls')),

    url(r'^empresa/', include('empresa.urls')),

    url(r'^oportunidad/', include('oportunidad.urls')),

    url(r'^mensaje/', include('mensaje.urls')),

    url(r'^contador_visitas/', include('contador_visitas.urls')),

    url(r'^disc/', include('disc.urls')),

    #ADMIN
    url(r'^admin/', include(admin.site.urls)),

    #LOGIN WITH SOACIAL
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'views.my_404_view'
from django.contrib import admin
from . import models
from .models import EmpresaRespuestas, PreguntaCultura, EmpresaCultura
from .cultura_empresarial import calcular_cultura_empresa

admin.site.register(models.PerfilCultura)

admin.site.register(models.PreguntaCultura)

class RespuestaCulturaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'descripcion', 'perfil_cultura')
admin.site.register(models.RespuestaCultura,RespuestaCulturaAdmin )

admin.site.register(models.CulturaMatrizDISC)

class EmpresaRespuestasAdmin(admin.ModelAdmin):
    list_display = ('empresa','pregunta', 'respuesta')
    def save_model(self, request, obj, form, change):
        if EmpresaRespuestas.objects.filter(empresa_id = obj.empresa.id).count() == PreguntaCultura.objects.filter().count():
            clan_total = EmpresaRespuestas.objects.filter(empresa_id = obj.empresa.id, respuesta__perfil_cultura = 1 ).count()
            adhocrata_total = EmpresaRespuestas.objects.filter(empresa_id = obj.empresa.id, respuesta__perfil_cultura = 2 ).count()
            jerarquica_total = EmpresaRespuestas.objects.filter(empresa_id = obj.empresa.id, respuesta__perfil_cultura = 3 ).count()
            racional_total = EmpresaRespuestas.objects.filter(empresa_id = obj.empresa.id, respuesta__perfil_cultura = 4 ).count()

            porcentaje_clan = clan_total * 12.5
            porcentaje_jerarquico = jerarquica_total * 12.5
            porcentaje_adhocrata = adhocrata_total * 12.5
            porcentaje_racional = racional_total * 12.5

            empresa_cultura, created = EmpresaCultura.objects.get_or_create(empresa_id = obj.empresa.id)
            if created is True:
                empresa_cultura.empresa = obj.empresa
            empresa_cultura.porcentaje_clan = porcentaje_clan
            empresa_cultura.porcentaje_adhocracia = porcentaje_adhocrata
            empresa_cultura.porcentaje_jerarquico = porcentaje_jerarquico
            empresa_cultura.porcentaje_racional = porcentaje_racional
            empresa_cultura.save()
        obj.save()

admin.site.register(models.EmpresaRespuestas, EmpresaRespuestasAdmin)

admin.site.register(models.EmpresaCultura)

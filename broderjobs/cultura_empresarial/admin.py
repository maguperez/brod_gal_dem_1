from django.contrib import admin
from . import models
from estudiante.models import Estudiante
from .models import EmpresaRespuestas, PreguntaCultura, EmpresaCultura, EstudianteCultura, EstudianteEmpresaCultura
from oportunidad.compatibilidad import actualizar_compatibilidad_empresa

admin.site.register(models.PerfilCultura)

admin.site.register(models.PreguntaCultura)

class RespuestaCulturaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'descripcion', 'perfil_cultura')
admin.site.register(models.RespuestaCultura,RespuestaCulturaAdmin )

admin.site.register(models.CulturaMatrizDISC)

class EmpresaRespuestasAdmin(admin.ModelAdmin):
    list_display = ('empresa','pregunta', 'respuesta')
    def save_model(self, request, obj, form, change):
        obj.save()
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

            for e in EstudianteCultura.objects.filter(estado='A'):
                est_empr_cultura, created = EstudianteEmpresaCultura.objects.get_or_create(estudiante_id = e.id,
                                                                                           empresa_id = empresa_cultura.empresa.id)
                if created is True:
                    est_empr_cultura.estudiante = e.estudiante
                    est_empr_cultura.empresa = empresa_cultura.empresa
                clan = (e.porcentaje_clan/100.00) * (empresa_cultura.porcentaje_clan/100.00)
                adhocracia = (e.porcentaje_adhocracia/100.00) *(empresa_cultura.porcentaje_adhocracia/100.00)
                jerarquica = (e.porcentaje_jerarquico/100.00) * (empresa_cultura.porcentaje_jerarquico/100.00)
                racional = (e.porcentaje_racional/100.00) * (empresa_cultura.porcentaje_racional/100.00)
                est_empr_cultura.compatibilidad_cultural = (clan*100) + (adhocracia*100) + (jerarquica*100) + (racional*100)
                est_empr_cultura.porcentaje_clan = clan
                est_empr_cultura.porcentaje_adhocracia = adhocracia
                est_empr_cultura.porcentaje_jerarquica = jerarquica
                est_empr_cultura.porcentaje_racional = racional
                est_empr_cultura.save()
                #Calcula la compatibilidad para todas las oportunidades dada el estudiante la empresa y la compatibilidad culrural entre ellos
                resp = actualizar_compatibilidad_empresa(est_empr_cultura.estudiante, empresa_cultura.empresa, est_empr_cultura.compatibilidad_cultural)


admin.site.register(models.EmpresaRespuestas, EmpresaRespuestasAdmin)

admin.site.register(models.EmpresaCultura)

admin.site.register(models.EstudianteCultura)


class EstudianteEmpresaCulturaAdmin(admin.ModelAdmin):
    list_display = ('estudiante','empresa', 'compatibilidad_cultural')
admin.site.register(models.EstudianteEmpresaCultura, EstudianteEmpresaCulturaAdmin )

from .models import EmpresaRespuestas, PreguntaCultura, EmpresaCultura
from empresa.models import Empresa


def calcular_cultura_empresa(empresa):
    
    if EmpresaRespuestas.objects.filter(empresa_id = empresa.id).count() == PreguntaCultura.objects.filter().count():
        clan_total = EmpresaRespuestas.objects.filter(empresa_id = empresa.id, respuesta_perfil_cultura = 1 ).count()
        adhocrata_total = EmpresaRespuestas.objects.filter(empresa_id = empresa.id, respuesta_perfil_cultura = 2 ).count()
        jerarquica_total = EmpresaRespuestas.objects.filter(empresa_id = empresa.id, respuesta_perfil_cultura = 3 ).count()
        racional_total = EmpresaRespuestas.objects.filter(empresa_id = empresa.id, respuesta_perfil_cultura = 4 ).count()

        porcentaje_clan = clan_total * 12.5
        porcentaje_jerarquico = jerarquica_total * 12.5
        porcentaje_adhocrata = adhocrata_total * 12.5
        porcentaje_racional = racional_total * 12.5

        empresa_cultura, created = EmpresaCultura.objects.get_or_create(empresa_id = empresa.id)
        if created is True:
            empresa_cultura.empresa = empresa
        empresa_cultura.porcentaje_clan = porcentaje_clan
        empresa_cultura.porcentaje_adhocracia = porcentaje_adhocrata
        empresa_cultura.porcentaje_jerarquico = porcentaje_jerarquico
        empresa_cultura.porcentaje_racional = porcentaje_racional
        empresa_cultura.save()
    return ''

from .models import EmpresaRespuestas, PreguntaCultura, EmpresaCultura, CulturaMatrizDISC, EstudianteCultura, EstudianteEmpresaCultura
from disc.models import EstudiantePatron
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

def calcular_cultura_estudiate(estudiante):
    try:
        disc_estudiante = EstudiantePatron.objects.get(estudiante_id = estudiante.id)
        cultura_clan = CulturaMatrizDISC.objects.get(orden = 1)
        cultura_jerarquica = CulturaMatrizDISC.objects.get(orden = 2)
        cultura_racional = CulturaMatrizDISC.objects.get(orden = 3)
        cultura_adhocracia = CulturaMatrizDISC.objects.get(orden = 4)

        disc = [int(i) for i in disc_estudiante.patron]

        delta_clan_d = abs(disc[0] - cultura_clan.letra_d)
        delta_clan_i = abs(disc[1] - cultura_clan.letra_i)
        delta_clan_s = abs(disc[2] - cultura_clan.letra_s)
        delta_clan_c = abs(disc[3] - cultura_clan.letra_c)
        total_delta_clan = delta_clan_d + delta_clan_i + delta_clan_s + delta_clan_c
        subtotal = total_delta_clan/4.00
        subtotal = subtotal * 14.28
        compatibilidad_clan =  100.00 - subtotal

        delta_adhocracia_d = abs(disc[0] - cultura_adhocracia.letra_d)
        delta_adhocracia_i = abs(disc[1] - cultura_adhocracia.letra_i)
        delta_adhocracia_s = abs(disc[2] - cultura_adhocracia.letra_s)
        delta_adhocracia_c = abs(disc[3] - cultura_adhocracia.letra_c)
        total_delta_adhocracia = delta_adhocracia_d + delta_adhocracia_i + delta_adhocracia_s + delta_adhocracia_c
        subtotal = total_delta_adhocracia/4.00
        subtotal = subtotal * 14.28
        compatibilidad_adhocracia = 100.00 - subtotal

        delta_jerarquica_d = abs(disc[0] - cultura_jerarquica.letra_d)
        delta_jerarquica_i = abs(disc[1] - cultura_jerarquica.letra_i)
        delta_jerarquica_s = abs(disc[2]- cultura_jerarquica.letra_s)
        delta_jerarquica_c = abs(disc[3] - cultura_jerarquica.letra_c)
        total_delta_jerarquica = delta_jerarquica_d + delta_jerarquica_i + delta_jerarquica_s + delta_jerarquica_c
        subtotal = total_delta_jerarquica/4.00
        subtotal = subtotal * 14.28
        compatibilidad_jerarquica =  100.00 - subtotal

        delta_racional_d = abs(disc[0] - cultura_racional.letra_d)
        delta_racional_i = abs(disc[1] - cultura_racional.letra_i)
        delta_racional_s = abs(disc[2] - cultura_racional.letra_s)
        delta_racional_c = abs(disc[3] - cultura_racional.letra_c)
        total_delta_racional = delta_racional_d + delta_racional_i + delta_racional_s + delta_racional_c
        subtotal = total_delta_racional/4.00
        subtotal = subtotal * 14.28
        compatibilidad_racional =  100.00 - subtotal

        estudiante_cultura, created = EstudianteCultura.objects.get_or_create(estudiante_id = estudiante.id)
        if created is True:
            estudiante_cultura.estudiante = estudiante
        estudiante_cultura.porcentaje_clan = compatibilidad_clan
        estudiante_cultura.porcentaje_adhocracia = compatibilidad_adhocracia
        estudiante_cultura.porcentaje_jerarquico = compatibilidad_jerarquica
        estudiante_cultura.porcentaje_racional = compatibilidad_racional
        estudiante_cultura.save()

        for empresa_cultura in EmpresaCultura.objects.filter(estado = 'A'):
            est_empr_cultura, created = EstudianteEmpresaCultura.objects.get_or_create(estudiante_id = estudiante.id,
                                                                                       empresa_id = empresa_cultura.empresa.id)
            if created is True:
                est_empr_cultura.estudiante = estudiante
                est_empr_cultura.empresa = empresa_cultura.empresa
            clan = (compatibilidad_clan/100.00) * (empresa_cultura.porcentaje_clan/100.00)
            adhocracia = (compatibilidad_adhocracia/100.00) *(empresa_cultura.porcentaje_adhocracia/100.00)
            jerarquica = (compatibilidad_jerarquica/100.00) * (empresa_cultura.porcentaje_jerarquico/100.00)
            racional = (compatibilidad_racional/100.00) * (empresa_cultura.porcentaje_racional/100.00)
            # est_empr_cultura.compatibilidad_cultural = (compatibilidad_clan * empresa_cultura.porcentaje_clan) +\
            #                                            (compatibilidad_adhocracia * empresa_cultura.porcentaje_adhocracia) + \
            #                                            (compatibilidad_jerarquica * empresa_cultura.porcentaje_jerarquico) + \
            #                                            (compatibilidad_racional * empresa_cultura.porcentaje_racional)
            est_empr_cultura.compatibilidad_cultural = (clan*100) + (adhocracia*100) + (jerarquica*100) + (racional*100)
            est_empr_cultura. porcentaje_clan = clan
            est_empr_cultura. porcentaje_adhocracia = adhocracia
            est_empr_cultura. porcentaje_jerarquica = jerarquica
            est_empr_cultura. porcentaje_racional = racional
            est_empr_cultura.save()
        return 1
    except:
        return -1
    return 0

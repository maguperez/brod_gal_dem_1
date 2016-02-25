from estudiante.models import Estudiante
from cultura_empresarial.models import EstudianteEmpresaCultura
from .models import Oportunidad
from django.db.models import Q
import operator

def calcular_compatibilidad(carrera, universidad, grado_estudio, empresa):
    filtros = []
    total = 0
    cultura = EstudianteEmpresaCultura.objects.filter(empresa_id = empresa, compatibilidad_cultural__gte = 20).values('estudiante_id')

    if '0' not in carrera:
        filtros.append(Q(carrera__in= carrera))

    if '0' not in universidad:
        filtros.append(Q(universidad__in= universidad))

    if grado_estudio is not None:
        filtros.append(Q(grado_estudio__in= grado_estudio))
    try:
        total = Estudiante.objects.filter(reduce(operator.and_, filtros )).count()
    except ValueError:
        error = ValueError
    return total



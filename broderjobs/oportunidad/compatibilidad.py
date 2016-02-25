from estudiante.models import Estudiante
from cultura_empresarial.models import EstudianteEmpresaCultura
from .models import Oportunidad, OportunidadCompatibilidad
from django.db.models import Q
import operator

def calcular_compatibilidad(carreras, universidades, grado_estudios, empresa):
    total_compatibles = 0
    estudiantes_cultura = EstudianteEmpresaCultura.objects.filter(empresa_id = empresa, compatibilidad_cultural__gte = 20).values('estudiante_id')
    estudiantes = Estudiante.objects.filter(pk__in = estudiantes_cultura)
    total_estudiantes = estudiantes.count()
    for e in estudiantes:
        carrera = 0
        universidad = 0
        grado_estudio = 0
        if '0' not in carreras and (e.carrera.id in map(int, carreras)):
            carrera = 11
        if '0' not in universidades and e.universidad.id in map(int, universidades):
            universidad = 5
        if grado_estudios != None and grado_estudios != '':
                if e.grado_estudio.id is int(grado_estudios):
                    grado_estudio = 11

        compatibilidad_academica =  carrera + universidad + grado_estudio
        if compatibilidad_academica > 10:
            total_compatibles =  total_compatibles + 1

    nivel = (total_compatibles * 100)/total_estudiantes if total_compatibles > 0 else 0
    data = {
        'total':total_compatibles,
        'nivel': nivel,
    }
    return data

def guardar_compatibilidad(carreras, universidades, grado_estudios, empresa, oportunidad_id):
    total_compatibles = 0
    estudiantes_cultura = EstudianteEmpresaCultura.objects.filter(empresa_id = empresa, compatibilidad_cultural__gte = 20).values('estudiante_id')
    estudiantes = Estudiante.objects.filter(pk__in = estudiantes_cultura)
    total_estudiantes = estudiantes.count()

    for e in estudiantes:
        carrera = 0
        universidad = 0
        grado_estudio = 0
        if '0' not in carreras and (e.carrera in carreras):
            carrera = 11
        if '0' not in universidades and e.universidad in universidades:
            universidad = 5
        if grado_estudios is not None and e.grado_estudio is grado_estudios:
            grado_estudio = 11

        compatibilidad_academica =  carrera + universidad + grado_estudio

        if oportunidad_id > 0:
            estudiante_cultura = estudiantes_cultura.get(estudiante_id = e.pk)
            c, created = OportunidadCompatibilidad.objects.get_or_create(estudiante_id = e.pk, oportunidad_id = oportunidad_id)
            if created:
                c.estudiante = e
            c.compatibilidad_academica = compatibilidad_academica
            c.compatibilidad_cultural = estudiante_cultura.compatibilidad_cultural
            c.compatibilidad_promedio = (c.compatibilidad_academica + c.compatibilidad_promedio) / 2
            c.save()

        if compatibilidad_academica > 10:
            total_compatibles =  total_compatibles + 1

    nivel = (total_compatibles * 100)/total_estudiantes if total_compatibles > 0 else 0
    data = {
        'total':total_compatibles,
        'nivel': nivel,
    }
    return data



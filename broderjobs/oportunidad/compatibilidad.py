from estudiante.models import Estudiante
from cultura_empresarial.models import EstudianteEmpresaCultura
from main.models import Idioma, Conocimiento
from .models import Oportunidad, OportunidadCompatibilidad
from django.db.models import Q
import operator
from main.utils import calular_edad

def calcular_compatibilidad(p_carreras, p_universidades, p_grado_estudios, p_edad_desde, p_edad_hasta, p_pais, p_ciudad,
                            p_genero, p_tipo_puesto, p_carga_horaria, p_idioma, p_conocimiento, p_empresa):
    total_compatibles = 0
    estudiantes_cultura = EstudianteEmpresaCultura.objects.filter(empresa_id = p_empresa, compatibilidad_cultural__gte = 20).values('estudiante_id')
    estudiantes = Estudiante.objects.filter(pk__in = estudiantes_cultura)
    total_estudiantes = estudiantes.count()
    for e in estudiantes:
        carrera = 0
        universidad = 0
        grado_estudio = 0
        edad = 0
        ubicacion = 0
        genero = 0
        tipo_puesto = 0
        carga_horaria = 0
        idioma = 0
        conocimiento = 0
        if '0' in p_carreras or (e.carrera.id in map(int, p_carreras)):
            carrera = 11
        if '0' in p_universidades or e.universidad.id in map(int, p_universidades):
            universidad = 5
        if p_grado_estudios == '0' or e.grado_estudio.id == int(p_grado_estudios):
            grado_estudio = 11
        if (p_edad_desde == '0' and p_edad_hasta == '0') or \
                (calular_edad(e.persona.fecha_nacimiento) in range(int(p_edad_desde), int(p_edad_hasta))):
            edad = 8
        if p_pais != '0':
            if p_ciudad != '0':
                if p_pais == e.pais.id:
                    ubicacion = 6
            else:
                if p_ciudad == e.ciudad.id:
                    ubicacion = 6
        else:
            ubicacion = 6
        if p_genero != '0' and p_genero != '':
            if e.persona.genero == p_genero:
                genero = 2
        if p_tipo_puesto == '0' or int(p_tipo_puesto) in  e.tipo_puesto.all() :
            tipo_puesto = 12
        if p_carga_horaria == '0' or e.carga_horaria.id == int(p_carga_horaria):
            carga_horaria = 11
        list_idioma = map(int, p_idioma)
        peso_idioma = 11/ len(list_idioma)
        if '0' in p_idioma:
            # or e.idioma.filter(id__in = map(int, p_idioma)).count() > 0 :
            idioma = 11
        else:
            for i in list_idioma:
                idioma_oportunidad = Idioma.objects.get(id = i)
                for x in e.idioma.filter():
                    if x.idiomabase == idioma_oportunidad.idiomabase and x.orden >= idioma_oportunidad.orden:
                        idioma = idioma + peso_idioma
                        break
        list_conocimiento = map(int, p_conocimiento)
        peso_conocimiento = 9 / len(list_conocimiento)
        if '0' in p_conocimiento:
                # or e.conocimiento.filter(id__in = map(int, p_conocimiento)).count() > 0 :
            conocimiento = 9
        else:
            for i in list_conocimiento:
                for x in e.conocimiento.filter():
                    if x.id == i:
                        conocimiento = conocimiento + peso_conocimiento
                        break

        compatibilidad_academica =  carrera + universidad + grado_estudio + edad + ubicacion + genero + tipo_puesto + idioma + \
                                    carga_horaria + conocimiento
        if compatibilidad_academica > 50:
            total_compatibles =  total_compatibles + 1

    nivel = (total_compatibles * 100)/total_estudiantes if total_compatibles > 0 else 0
    data = {
        'total':total_compatibles,
        'nivel': nivel,
    }
    return data

def guardar_compatibilidad(p_carreras, p_universidades, p_grado_estudios, p_edad_desde, p_edad_hasta, p_pais, p_ciudad,
                           p_genero, p_tipo_puesto, p_carga_horaria, p_idioma, p_conocimiento, p_empresa, p_oportunidad_id):
    try:
        total_compatibles = 0
        estudiantes_cultura = EstudianteEmpresaCultura.objects.filter(empresa_id = p_empresa, compatibilidad_cultural__gte = 20).values('estudiante_id')
        estudiantes = Estudiante.objects.filter(pk__in = estudiantes_cultura)
        total_estudiantes = estudiantes.count()

        for e in estudiantes:
            carrera = 0
            universidad = 0
            grado_estudio = 0
            edad = 0
            ubicacion = 0
            genero = 0
            tipo_puesto = 0
            carga_horaria = 0
            idioma = 0
            conocimiento = 0
            if e.carrera in p_carreras or p_carreras is None:
                carrera = 11
            if e.universidad in p_universidades or p_universidades is None:
                universidad = 5
            if p_grado_estudios is None or e.grado_estudio == p_grado_estudios:
                grado_estudio = 11
            if e.persona.fecha_nacimiento is not None :
                if (p_edad_desde == '' and p_edad_hasta == ''):
                    if calular_edad(e.persona.fecha_nacimiento) in range(int(p_edad_desde), int(p_edad_hasta)):
                        edad = 8
            if p_pais != None:
                if p_ciudad != None:
                    if p_pais == e.pais.id:
                        ubicacion = 6
                else:
                    if p_ciudad == e.ciudad.id:
                        ubicacion = 6
            else:
                ubicacion = 6
            if p_genero == None or e.persona.genero == p_genero:
                genero = 2
            if p_tipo_puesto == None or p_tipo_puesto in e.tipo_puesto.all():
                genero = 12
            if p_carga_horaria == None or e.carga_horaria == p_carga_horaria:
                genero = 11
            # if p_idioma is None or e.idioma.filter(id__in = p_idioma.all().values('id')):
            #     idioma = 11
            # if p_conocimiento is None or e.conocimiento.filter(id__in = p_conocimiento.all().values('id')):
            #     conocimiento = 11
            if p_idioma:
            # or e.idioma.filter(id__in = map(int, p_idioma)).count() > 0 :
                idioma = 11
            else:
                peso_idioma = 11/ p_idioma.count()
                for i in p_idioma.all():
                    for x in e.idioma.filter():
                        if x.idiomabase == i.idiomabase and x.orden >= i.orden:
                            idioma = idioma + peso_idioma
                            break
            if p_conocimiento:
                # or e.conocimiento.filter(id__in = map(int, p_conocimiento)).count() > 0 :
                conocimiento = 9
            else:
                peso_conocimiento = 9 / p_conocimiento.count()
                for i in p_conocimiento.all():
                    for x in e.conocimiento.filter():
                        if x.id == i.id:
                            conocimiento = conocimiento + peso_conocimiento
                            break

            compatibilidad_academica =  carrera + universidad + grado_estudio + edad + ubicacion + genero + tipo_puesto + idioma + \
                                        carga_horaria + conocimiento

            if p_oportunidad_id > 0:
                    estudiante_cultura = EstudianteEmpresaCultura.objects.get(estudiante_id = e.pk, empresa_id = p_empresa.id )
                    c, created = OportunidadCompatibilidad.objects.get_or_create(estudiante_id = e.pk, oportunidad_id = p_oportunidad_id)
                    if created:
                        c.estudiante = e
                    c.oportunidad.id = p_oportunidad_id
                    c.compatibilidad_academica = compatibilidad_academica
                    c.compatibilidad_cultural = estudiante_cultura.compatibilidad_cultural
                    c.compatibilidad_promedio = (c.compatibilidad_academica + c.compatibilidad_cultural) / 2
                    c.save()

            if compatibilidad_academica > 10:
                total_compatibles =  total_compatibles + 1

        nivel = (total_compatibles * 100)/total_estudiantes if total_compatibles > 0 else 0
    except:
        total_compatibles= 0
        nivel= 0

    data = {
        'total':total_compatibles,
        'nivel': nivel,
    }
    return data



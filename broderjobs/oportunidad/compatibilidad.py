from estudiante.models import Estudiante
from cultura_empresarial.models import EstudianteEmpresaCultura
from main.models import Idioma, Conocimiento
from .models import Oportunidad, OportunidadCompatibilidad
from django.db.models import Q, F
import operator
from main.utils import calular_edad
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

def calcular_compatibilidad(p_carreras, p_universidades, p_grado_estudios, p_edad_desde, p_edad_hasta, p_pais, p_ciudad,
                            p_genero, p_tipo_puesto, p_carga_horaria, p_idioma, p_conocimiento, p_remuneracion_min,
                            p_remuneracion_max, p_empresa):
    total_compatibles = 0
    estudiantes_cultura = EstudianteEmpresaCultura.objects.filter(empresa_id = p_empresa, compatibilidad_cultural__gte = 20).values('estudiante_id')
    estudiantes = Estudiante.objects.filter(pk__in = estudiantes_cultura)
    total_estudiantes = estudiantes.count()

    mylist = []
    if '0' not in p_carreras:
        mylist.append((Q(carrera__in=p_carreras)))
    if '0' not in p_universidades :
        mylist.append((Q(universidad__in = p_universidades)))
    if p_grado_estudios != '0':
        mylist.append((Q(grado_estudio_id = int(p_grado_estudios))))
    if p_edad_desde != '0' and p_edad_desde != '' and p_edad_hasta != '0' and p_edad_hasta != '':
        # mylist = [Q(edad__range=(int(p_edad_desde),int(p_edad_hasta)))]
        desde = datetime.now() - relativedelta(years= int(p_edad_desde))
        hasta = datetime.now() - relativedelta(years= int(p_edad_hasta))
        mylist.append((Q(persona__fecha_nacimiento__range = [hasta,desde])))
    if p_pais != '0':
        if p_ciudad != '0' and p_ciudad != '':
            mylist.append(Q(ciudad_id= int(p_ciudad)), Q(pais_id= int(p_pais)))
        else:
            mylist.append((Q(pais_id= int(p_pais))))
    if p_genero != '0' and p_genero != '':
        mylist.append((Q(persona__genero= p_genero)))
    if p_tipo_puesto != '0' and  p_tipo_puesto != '':
         mylist.append((Q(tipo_puesto__in= [p_tipo_puesto])))
    if p_carga_horaria != '0' and  p_carga_horaria != '':
        mylist.append((Q(carga_horaria_id= int(p_carga_horaria))))
    # if p_idioma != '0' and p_idioma !='':
    #     mylist = [Q(idioma__idiomabase__in= int(p_carga_horaria))]
    # for e in estudiantes:
    #     carrera = 0
    #     universidad = 0
    #     grado_estudio = 0
    #     edad = 0
    #     ubicacion = 0
    #     genero = 0
    #     tipo_puesto = 0
    #     carga_horaria = 0
    #     idioma = 0
    #     conocimiento = 0
    #     if '0' in p_carreras or (e.carrera.id in map(int, p_carreras)):
    #         carrera = 11
    #     if '0' in p_universidades or e.universidad.id in map(int, p_universidades):
    #         universidad = 5
    #     if p_grado_estudios == '0' or e.grado_estudio.id == int(p_grado_estudios):
    #         grado_estudio = 11
    #     if p_edad_desde == '0' and p_edad_hasta == '0':
    #         edad = 8
    #     elif e.persona.fecha_nacimientois is not None:
    #         if calular_edad(e.persona.fecha_nacimiento ) in range(int(p_edad_desde), int(p_edad_hasta)):
    #             edad = 8
    #     if p_pais != '0':
    #         if p_ciudad != '0':
    #             if int(p_ciudad) == e.ciudad.id:
    #                 ubicacion = 6
    #         else:
    #             if int(p_pais) == e.pais.id:
    #                 ubicacion = 6
    #     else:
    #         ubicacion = 6
    #     if p_genero != '0' and p_genero != '':
    #         if e.persona.genero == p_genero:
    #             genero = 2
    #     else:
    #         genero = 2
    #     if p_tipo_puesto == '0' or e.tipo_puesto.filter(id = int(p_tipo_puesto)).count() > 0 :
    #         tipo_puesto = 12
    #     if p_carga_horaria == '0' or e.carga_horaria.id == int(p_carga_horaria):
    #         carga_horaria = 11
    #     list_idioma = map(int, p_idioma)
    #     peso_idioma = 11/ len(list_idioma)
    #     if '0' in p_idioma:
    #         # or e.idioma.filter(id__in = map(int, p_idioma)).count() > 0 :
    #         idioma = 11
    #     else:
    #         for i in list_idioma:
    #             idioma_oportunidad = Idioma.objects.get(id = i)
    #             for ii in e.idioma.filter():
    #                 if ii.idiomabase == idioma_oportunidad.idiomabase and ii.orden >= idioma_oportunidad.orden:
    #                     idioma = idioma + peso_idioma
    #                     break
    #     list_conocimiento = map(int, p_conocimiento)
    #     peso_conocimiento = 9 / len(list_conocimiento)
    #     if '0' in p_conocimiento:
    #             # or e.conocimiento.filter(id__in = map(int, p_conocimiento)).count() > 0 :
    #         conocimiento = 9
    #     else:
    #         for c in list_conocimiento:
    #             for cc in e.conocimiento.filter():
    #                 if cc.id == c:
    #                     conocimiento = conocimiento + peso_conocimiento
    #                     break
    #
    #     compatibilidad_academica =  carrera + universidad + grado_estudio + edad + ubicacion + genero + tipo_puesto + idioma + \
    #                                 carga_horaria + conocimiento
    #     if compatibilidad_academica > 50:
    #         total_compatibles =  total_compatibles + 1
    if len(mylist) > 0:
        total_compatibles = Estudiante.objects.filter(reduce(operator.and_, mylist)).count()

    else:
        total_compatibles = total_estudiantes
    nivel = (total_compatibles * 100)/total_estudiantes if total_compatibles > 0 else 0
    data = {
        'total':total_compatibles,
        'nivel': nivel,
    }
    return data

def guardar_compatibilidad(oportunidad):
    try:
        total_compatibles = 0
        estudiantes_cultura = EstudianteEmpresaCultura.objects.filter(empresa_id = oportunidad.empresa,
                                                                      compatibilidad_cultural__gte = 20).values('estudiante_id')
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
            if  oportunidad.carrera.all() == 0 or  e.carrera in oportunidad.carrera.all():
                carrera = 11
            if oportunidad.universidad.filter().count() == 0 or e.universidad in oportunidad.universidad.all():
                universidad = 5
            if oportunidad.grado_estudio is None or e.grado_estudio == oportunidad.grado_estudio:
                grado_estudio = 11
            if( oportunidad.edad_desde == '' or oportunidad.edad_desde is None) or \
                    (oportunidad.edad_hasta == '' or oportunidad.edad_hasta is None):
                edad = 8
            elif e.persona.fecha_nacimiento is not None :
                if calular_edad(e.persona.fecha_nacimiento) in range(int(oportunidad.edad_desde), int(oportunidad.edad_hasta)):
                    edad = 8
            if oportunidad.pais != None:
                if oportunidad.ciudad != None:
                    if oportunidad.ciudad == e.ciudad:
                        ubicacion = 6
                else:
                    if oportunidad.pais == e.pais:
                        ubicacion = 6
            else:
                ubicacion = 6
            if oportunidad.genero == None or e.persona.genero == oportunidad.genero:
                genero = 2
            if oportunidad.tipo_puesto == None or e.tipo_puesto.filter(id = oportunidad.tipo_puesto.id).count()>0:
                tipo_puesto = 12
            if oportunidad.carga_horaria == None or e.carga_horaria == oportunidad.carga_horaria:
                carga_horaria = 11
            if oportunidad.idioma.count() == 0:
                idioma = 11
            else:
                peso_idioma = 11/ oportunidad.idioma.count()
                for i in oportunidad.idioma.all():
                    for x in e.idioma.filter():
                        if x.idiomabase == i.idiomabase and x.orden >= i.orden:
                            idioma = idioma + peso_idioma
                            break
            if oportunidad.conocimiento.count() == 0:
                # or e.conocimiento.filter(id__in = map(int, p_conocimiento)).count() > 0 :
                conocimiento = 9
            else:
                peso_conocimiento = 9 / oportunidad.conocimiento.count()
                for i in oportunidad.conocimiento.all():
                    for x in e.conocimiento.filter():
                        if x.id == i.id:
                            conocimiento = conocimiento + peso_conocimiento
                            break

            compatibilidad_academica =  carrera + universidad + grado_estudio + edad + ubicacion + genero + tipo_puesto \
                                        + idioma + carga_horaria + conocimiento

            if oportunidad.id > 0:
                    estudiante_cultura = EstudianteEmpresaCultura.objects.get(estudiante_id = e.pk,
                                                                              empresa_id = oportunidad.empresa.id )
                    c, created = OportunidadCompatibilidad.objects.get_or_create(estudiante_id = e.pk,
                                                                                 oportunidad_id = oportunidad.id)
                    if created:
                        c.estudiante = e
                    c.oportunidad.id = oportunidad.id
                    c.compatibilidad_academica = compatibilidad_academica
                    c.compatibilidad_cultural = estudiante_cultura.compatibilidad_cultural
                    c.compatibilidad_promedio = (c.compatibilidad_academica + c.compatibilidad_cultural) / 2
                    c.estado = oportunidad.estado
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

def actualizar_compatibilidad(estudiante):
    try:
    # if estudiante.id > 0:
        oportunidades = Oportunidad.objects.filter(estado = 'A')

        for oportunidad in oportunidades.all():
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
            if oportunidad.carrera.all() == 0 or estudiante.carrera.id in oportunidad.carrera.all() :
                carrera = 11
            if oportunidad.universidad.all() == 0 or estudiante.universidad in oportunidad.universidad.all() :
                universidad = 5
            if oportunidad.grado_estudio is None or estudiante.grado_estudio == oportunidad.grado_estudio:
                grado_estudio = 11
            if (oportunidad.edad_desde == '' or oportunidad.edad_desde is None) or \
                    (oportunidad.edad_hasta == '' or oportunidad.edad_hasta is None):
                edad = 8
            elif estudiante.persona.fecha_nacimiento is not None :
                if calular_edad(estudiante.persona.fecha_nacimiento) in range(int(oportunidad.edad_desde),
                                                                              int(oportunidad.edad_hasta)):
                    edad = 8
            if oportunidad.pais != None:
                if oportunidad.ciudad != None:
                    if oportunidad.ciudad == estudiante.ciudad:
                        ubicacion = 6
                else:
                    if oportunidad.pais == estudiante.pais:
                        ubicacion = 6
            else:
                ubicacion = 6
            if oportunidad.genero == None or estudiante.persona.genero == oportunidad.genero:
                genero = 2
            if oportunidad.tipo_puesto == None or oportunidad.tipo_puesto in estudiante.tipo_puesto.all():
                tipo_puesto = 12
            if oportunidad.carga_horaria == None or estudiante.carga_horaria == oportunidad.carga_horaria:
                carga_horaria = 11
            if oportunidad.idioma.count() == 0:
                idioma = 11
            else:
                peso_idioma = 11/ oportunidad.idioma.count()
                for i in oportunidad.idioma.all():
                    for x in estudiante.idioma.filter():
                        if x.idiomabase == i.idiomabase and x.orden >= i.orden:
                            idioma = idioma + peso_idioma
                            break
            if oportunidad.conocimiento.count() == 0:
                conocimiento = 9
            else:
                peso_conocimiento = 9 /oportunidad.conocimiento.count()
                for i in oportunidad.conocimiento.all():
                    for x in estudiante.conocimiento.filter():
                        if x.id == i.id:
                            conocimiento = conocimiento + peso_conocimiento
                            break

            compatibilidad_academica =  carrera + universidad + grado_estudio + edad + ubicacion + genero + tipo_puesto + idioma + \
                                        carga_horaria + conocimiento

            try:
                estudiante_cultura, create_ec = EstudianteEmpresaCultura.objects.get_or_create(estudiante_id = estudiante.pk,
                                                                                     empresa_id = oportunidad.empresa.id )
                if create_ec:
                    estudiante_cultura.estudiante = estudiante
                    estudiante_cultura.empresa = oportunidad.empresa
                    estudiante_cultura.compatibilidad_cultural = 0
                    estudiante_cultura.save()
                oportunidad_comp, create = OportunidadCompatibilidad.objects.get_or_create(oportunidad_id = oportunidad.id,
                                                                                       estudiante_id = estudiante.id)
                if create:
                    oportunidad_comp.estudiante = estudiante
                    oportunidad_comp.oportunidad = oportunidad
                oportunidad_comp.compatibilidad_academica = compatibilidad_academica
                oportunidad_comp.compatibilidad_cultural = estudiante_cultura.compatibilidad_cultural
                oportunidad_comp.compatibilidad_promedio = (oportunidad_comp.compatibilidad_academica + oportunidad_comp.compatibilidad_cultural) / 2
                oportunidad_comp.save()
                data = "ok"
            except:
                data= "error"
    except:
        data = "error"
    return data



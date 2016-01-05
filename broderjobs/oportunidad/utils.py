# coding=utf-8
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, Conocimiento
from empresa.models import Empresa, Puesto
from estudiante.models import Estudiante


def obtener_candidatos (objects):
    data_dict = {}
    data_records=[]
    for p in objects:
        estudiante = Estudiante.objects.get(pk = p.estudiante.id)
        id = str(p.id)
        nombre = str(estudiante.persona)
        universidad = str(estudiante.universidad)
        carrera = str(estudiante.carrera)
        graduacion = "Sem " + str(estudiante.semestre_graduacion) + " del año " + str(estudiante.ano_graduacion)
        fecha_postulacion = str(p.fecha_creacion)
        compatibilidad = "60%"
        records = {"checkbox":"", "id":id, "nombre":nombre,"universidad":universidad,"carrera":carrera,
                    "graduacion":graduacion, "fecha_postulacion": fecha_postulacion, "compatibilidad": compatibilidad,
                   "botones":""}
        data_records.append(records)

    return data_records

    # resp = []
    # for p in objects:
    # #     data = []
    #     estudiante = Estudiante.objects.get(pk = p.estudiante.id)
    #     data.append("")
    #     data.append( str(estudiante.id))
    #     data.append(str(estudiante))
    #     data.append(str(estudiante.universidad))
    #     data.append(str(estudiante.carrera))
    #     data.append("Sem " + str(estudiante.semestre_graduacion) + " del año " + str(estudiante.ano_graduacion))
    #     data.append(str(p.fecha_creacion))
    #     data.append("60%")
    #     data.append("")
    #     resp.append(data)
    # return resp








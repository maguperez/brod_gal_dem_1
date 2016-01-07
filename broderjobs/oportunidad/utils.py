# coding=utf-8
from broderjobs import constants
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, Conocimiento
from empresa.models import Empresa, Puesto
from estudiante.models import Estudiante
from .models import Oportunidad, Postulacion, ProcesoFase


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
        records = {"checkbox":"", "id":id, "id_estudiante": estudiante.id, "nombre":nombre,"universidad":universidad,"carrera":carrera,
                    "graduacion":graduacion, "fecha_postulacion": fecha_postulacion, "compatibilidad": compatibilidad,
                   "botones":"", "estado": p.estado, "estado_fase": p.estado_fase}
        data_records.append(records)

    return data_records










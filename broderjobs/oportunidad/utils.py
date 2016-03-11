# coding=utf-8
from broderjobs import constants
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, Conocimiento
from empresa.models import Empresa, Puesto
from estudiante.models import Estudiante
from .models import Oportunidad, Postulacion, ProcesoFase, OportunidadCompatibilidad


def obtener_candidatos (objects):
    data_dict = {}
    data_records=[]
    for p in objects:
        estudiante = Estudiante.objects.get(pk = p.estudiante.id)
        try:
            compatibilidad = OportunidadCompatibilidad.objects.get(estudiante_id = estudiante.id,
                                                                   oportunidad_id = p.oportunidad_id)
        except Exception, e:
            compatibilidad = OportunidadCompatibilidad()
            data = str(e)
        id = str(p.id)
        nombre = str(estudiante.persona)
        universidad = str(estudiante.universidad)
        carrera = str(estudiante.carrera)
        graduacion = "Ciclo " + str(estudiante.semestre_graduacion) + " del año " + str(estudiante.ano_graduacion)
        fecha_postulacion = str(p.fecha_creacion)
        compatibilidad = str(compatibilidad.compatibilidad_promedio)+ "%"
        records = {"checkbox":"", "id":id, "id_estudiante": estudiante.id, "nombre":nombre,"universidad":universidad,
                   "carrera":carrera,"graduacion":graduacion, "fecha_postulacion": fecha_postulacion,
                   "compatibilidad": compatibilidad,"botones":"", "estado": p.estado,
                   "estado_fase": p.estado_fase}
        data_records.append(records)

    return data_records










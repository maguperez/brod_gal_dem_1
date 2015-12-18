# coding=utf-8
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, Conocimiento
from empresa.models import Empresa, Puesto
from estudiante.models import Estudiante


def obtener_candidatos (objects):
    resp = []
    for p in objects:
        data = []
        estudiante = Estudiante.objects.get(pk = p.estudiante.id)
        data.append(str(estudiante))
        data.append(str(estudiante.universidad))
        data.append(str(estudiante.carrera))
        data.append("Sem " + str(estudiante.semestre_graduacion) + " del año " + str(estudiante.ano_graduacion))
        data.append(str(p.fecha_creacion))
        resp.append(data)
    return resp



# coding=utf-8
from datetime import date, datetime
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

def calular_edad(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#carga el rago de años para el select
def anos_rango():
    anos = []
    for y in range(1980,2020):
        anos.append((str(y), str(y)))
    return [('','Años')] + anos

#carga el rango de semestre para el  select
def semestre_rango():
    semestres = []
    for y in range(1,3):
        semestres.append((str(y), "Ciclo " + str(y)))
    return [('', 'Ciclos')] + semestres

#carga el rango de semestre para el  select
def dias_del_mes():
    dias = []
    for y in range(1,32):
        dias.append((y, y))
    return [('','Dia')] + dias

def meses_del_ano():
    meses = []
    for y in range(1,13):
        meses.append((y, y))
    return [('','Mes')] + meses

def anos_nacimiento():
    anos = []
    for y in range(date.today().year - 40, (date.today().year - 17)):
        anos.append((y, y))
    return [('','Año')] + anos

def estado_oportunidad():
    anos = []
    anos.append(('P', 'Archivado'))
    anos.append(('A', 'Abierto'))
    anos.append(('C', 'Cerrado'))
    return anos

def estado_postulacion():
    anos = []
    anos.append(('P', 'Postulacion'))
    anos.append(('E', 'En Evaluacion'))
    anos.append(('F', 'Finalizado'))
    return anos

def estado_mensaje():
    anos = []
    anos.append(('G', 'Guardado'))
    anos.append(('E', 'Eliminado'))
    return anos

def estado_registro():
    anos = []
    anos.append(('A', 'Activo'))
    anos.append(('I', 'Inactivado'))
    return anos

def genero():
    anos = []
    anos.append(('M', 'Masculino'))
    anos.append(('F', 'Femenino'))
    return anos








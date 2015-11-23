# coding=utf-8
from datetime import date, datetime

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
    for y in range(0,3):
        semestres.append((str(y), str(y)))
    return [('', 'Semestre')] + semestres

#carga el rango de semestre para el  select
def dias_del_mes():
    dias = []
    for y in range(1,31):
        dias.append((y, y))
    return [('','Dia')] + dias

def meses_del_ano():
    meses = []
    for y in range(1,12):
        meses.append((y, y))
    return [('','Mes')] + meses

def anos_nacimiento():
    anos = []
    for y in range(1950, (date.today().year - 10)):
        anos.append((y, y))
    return [('','Año')] + anos

def estado_oportunidad():
    anos = []
    anos.append(('Pediente', 'P'))
    anos.append(('Abierto', 'A'))
    anos.append(('Cerrado', 'C'))
    return anos





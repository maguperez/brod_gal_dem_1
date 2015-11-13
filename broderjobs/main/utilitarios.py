# coding=utf-8
from datetime import date

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

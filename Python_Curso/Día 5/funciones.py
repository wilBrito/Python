from random import *

lista_numeros = [1, 5, 3, 9]


def lanzar_moneda():
    moneda = ''
    sorteo = randint(0, 2)
    if sorteo == 0:
        moneda = 'Cara'
    else:
        moneda = 'Cruz'
    return moneda

print(lanzar_moneda())
def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        print("La lista se autodestruirá")
        lista.clear()
    else:
        print("La lista se salva")
    return lista


def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(valor)
    return lista

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    resultado = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            valor_col2 = int(columnas[1])
            pares_col4 = columnas[3].split(',')

            for par in pares_col4:
                letra = par.split(':')[0]
                if letra in resultado:
                    resultado[letra] += valor_col2
                else:
                    resultado[letra] = valor_col2

    return dict(sorted(resultado.items()))

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    resultado = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            letra = columnas[0]
            pares_col5 = columnas[4].split(',')

            suma_valores = sum(int(par.split(':')[1]) for par in pares_col5)

            if letra in resultado:
                resultado[letra] += suma_valores
            else:
                resultado[letra] = suma_valores

    return dict(sorted(resultado.items()))
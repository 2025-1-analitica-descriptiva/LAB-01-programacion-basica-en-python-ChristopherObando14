"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open("files/input/data.csv", "r") as archivo:
        conteo_letras = {}
        for linea in archivo:
            columnas = linea.strip().split('\t')
            if columnas:
                letra = columnas[0]
                valor = int(columnas[1])
                if letra in conteo_letras:
                    conteo_letras[letra] += valor
                else:
                    conteo_letras[letra] = valor

    resultado = [(letra, suma) for letra, suma in conteo_letras.items()]
    resultado.sort(key=lambda x: x[0])
    return resultado




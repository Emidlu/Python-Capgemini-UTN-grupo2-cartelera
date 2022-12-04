
import json


def agregarIterableJson(diccionario, iterable):

    for elemento in iterable:
        agregarElementoJson(diccionario, str(elemento))




def agregarElementoJson(diccionario, elemento):

    file_text = open('elementosEliminados.json', 'r')
    data = file_text.read()
    file_text.close()

    datosConvertidos = json.loads(data)

    datosConvertidos[0][diccionario].append(elemento)

    nuevoJson = json.dumps(datosConvertidos)

    jsonFile=open('elementosEliminados.json', 'w')
    jsonFile.write(nuevoJson)
    jsonFile.close()







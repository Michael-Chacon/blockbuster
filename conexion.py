import json

def descargarJson(archivo):
    data = {}
    with open(f"dataBase/{archivo}.json", "r") as f:
        data = json.loads(f.read())
    return data


def guardarJson(archivo, diccionario):
    with open(f"dataBase/{archivo}.json", "w+") as f:
        f.write(json.dumps(diccionario, indent=3))

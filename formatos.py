from conexion import *
from utils import generarId

def guardarFormatos():
    formatos = descargarJson("formatos")
    id = generarId("formatos")
    nombre = input("Ingrese el nombre: ")
    formatos[id] = {"nombre" : nombre}

    guardarJson("formatos", formatos)


def listarFormatos():
    formatos = descargarJson("formatos")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in formatos.items():
        print(f"{llave} \t|{valor['nombre']}")
        print(40 * "-")



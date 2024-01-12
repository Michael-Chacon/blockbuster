from conexion import *
from utils import *

def guardarFormatos():
    bandera = True
    while bandera:
        formatos = descargarJson("formatos")
        id = generarId("formatos")
        print("Ingrese el nombre: ")
        nombre = validar(str)
        formatos[id] = {"nombre" : nombre}
        guardarJson("formatos", formatos)
        bandera = romperCiclo("Quiere almacenar otro formato? ")


def listarFormatos():
    formatos = descargarJson("formatos")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in formatos.items():
        print(f"{llave} \t|{valor['nombre']}")
        print(40 * "-")



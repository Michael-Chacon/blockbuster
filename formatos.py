from conexion import *

def guardarFormatos():
    formatos = descargarJson("formatos")
    id = 44
    nombre = input("Ingrese el nombre: ")
    formatos[44] = {"nombre" : nombre}

    guardarJson("formatos", formatos)


def listarFormatos():
    formatos = descargarJson("formatos")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in formatos.items():
        print(f"{llave} \t|{valor['nombre']}")
        print(40 * "-")



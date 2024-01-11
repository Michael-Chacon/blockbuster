from conexion import *

def guardarGenero():
    generos = descargarJson("generos")
    id = 44
    nombre = input("Ingrese el nombre: ")
    generos[44] = {"nombre" : nombre}

    guardarJson("generos", generos)


def listarGeneros():
    generos = descargarJson("generos")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in generos.items():
        print(f"{llave} \t|{valor['nombre']}")
        print(40 * "-")



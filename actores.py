from conexion import *

def guardarActor():
    actores = descargarJson("actores")
    id = 44
    nombre = input("Ingrese el del actor: ")
    actores[44] = {"nombre" : nombre}

    guardarJson("actores", actores)


def listarActores():
    actores = descargarJson("actores")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in actores.items():
        print(f"{llave} \t|{valor['nombre']}")
        print(40 * "-")



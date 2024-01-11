from conexion import *
from utils import generarId

def guardarActor():
    actores = descargarJson("actores")
    id = generarId("peliculas")
    nombre = input("Ingrese el del actor: ")
    actores[id] = {"nombre" : nombre}

    guardarJson("actores", actores)


def listarActores():
    actores = descargarJson("actores")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in actores.items():
        print(f"{llave} \t|{valor['nombre']}")
        print(40 * "-")



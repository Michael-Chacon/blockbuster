from conexion import *
from utils import *

def guardarActor():
    bandera = True
    while bandera:
        actores = descargarJson("actores")
        id = generarId("actores")
        nombre = input("Ingrese el del actor: ")
        actores[id] = {"nombre" : nombre}
        guardarJson("actores", actores)
        bandera = romperCiclo("Quiere almacenar otro actor? ")


def listarActores():
    actores = descargarJson("actores")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in actores.items():
        print(f"{llave} \t|{valor['nombre']}")
        print(40 * "-")
    



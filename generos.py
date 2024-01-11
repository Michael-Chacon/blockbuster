from conexion import *
from utils import *

def guardarGenero():
    bandera = True
    while bandera:
        generos = descargarJson("generos")
        id = generarId("generos")
        nombre = input("Ingrese el nombre: ")
        generos[id] = {"nombre" : nombre}
        guardarJson("generos", generos)
        bandera = romperCiclo("\nQuiere registrar otro genero?")

def listarGeneros():
    generos = descargarJson("generos")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in generos.items():
        print(f"{llave} \t|{valor['nombre']}")
        print(40 * "-")
    



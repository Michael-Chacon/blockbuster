from conexion import *
from utils import *

def guardarGenero():
    bandera = True
    while bandera:
        generos = descargarJson("generos")
        id = generarId("generos")
        print("Ingrese el nombre: ")
        nombre = validar(str)
        generos[id] = {"nombre" : nombre}
        guardarJson("generos", generos)
        bandera = romperCiclo("\nQuiere registrar otro genero?")

def listarGeneros():
    generos = descargarJson("generos")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in generos.items():
        print(f"{llave} \t| {valor['nombre'].title()}")
        print(40 * "-")
    



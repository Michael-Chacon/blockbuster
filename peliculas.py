import os
from utils import *
from conexion import *
from generos import listarGeneros
from actores import listarActores
from formatos import listarFormatos

def agregarPelicula():
    generos = descargarJson("generos")
    actores = descargarJson("actores")
    formatos = descargarJson("formatos")
    peliculas = descargarJson("peliculas")

    banderaMain = True
    while banderaMain:
        os.system("clear")
        print("\n--- Agregar Peliculas ---\n")
        id = generarId("peliculas")
        print("agregar pelicula")
        print("Nombre: ")
        nombre = validar(str)
        print("Género: ")
        bandera = True
        gen = {}
        while bandera:
            listarGeneros()
            idGenero = input("Seleccione el genero por el id: ")
            if idGenero not in generos:
                print("El id no existe")
            else:
                gen[idGenero] = {"id": idGenero, "nombre": generos[idGenero]["nombre"]}  
            bandera = romperCiclo("Quiere agregar otro genero?")
        
        duracion = input("Duración: ")
        
        sinopsis = input("Sinopsis\n: ")

        print("Seleccionar actores\n")
        act = {}
        banderaA = True
        while banderaA:
            listarActores()
            idActor = input("Escriba el id del actor: ")
            if idActor not in actores:
                print("El id no existe")
            else:
                rol = input("Que rol tiene el actor\n\t1. Protagonista \n\t2. Antagonista \n\t3. Extra\n:")
                if rol == '1':
                    rolR = 'Protagonista'
                elif rol == '2':
                    rolR = 'Antogonista'
                elif rol == '3':
                    rolR = 'Extra'
                else:
                    print("El rol seleccionado no existe")
                act[idActor] = {"id": idActor, "nombre": actores[idActor]["nombre"], "rol": rolR}
            banderaA = romperCiclo("Quiere agregar otro actor?")

        print("Seleccionar formatos:\n")
        form = {}
        banderaF = True
        while banderaF:
            listarFormatos()
            idFormato = input("Escriba el id del formato: ")
            if idFormato not in formatos:
                print("El id no existe")
            else:
                copias = input("Numero de copias: ")
                valorPrestamo = input("Valor Prestamo: ")
                form[idFormato] = {"id": idFormato, "nombre": formatos[idFormato]['nombre'], "NroCopias": copias, "valorPrestamo": valorPrestamo}
            banderaF = romperCiclo("Quiere agregar otro formato?")

        peliculas[id] = {"id": id, "nombre": nombre.lower(), "duracion": duracion, "sinopsis": sinopsis, "generos": gen, "actores": act, "formato": form}
        guardarJson("peliculas", peliculas)
        print("\n--- Pelicula registrada con éxito ---\n")
        banderaMain = romperCiclo("Quiere agregar otra pelicula? ")


def eliminarPelicula():
    bandera = True
    while bandera:
        print("\n--- Eliminar Peliculas ---\n")
        peliculas = descargarJson("peliculas")
        listarIdNomabre()
        idPelicula = input("Seleccione la pelicula por su id: ")
        if idPelicula not in peliculas:
            print(f"No existe una  pelicula con el id {id}")
        else:
            del peliculas[idPelicula]
            guardarJson("peliculas", peliculas)
            print("--- Pelicula eliminada con éxito")
        bandera = romperCiclo("Quiere eliminar otra pelicula? ")


def eliminarActorDPelicula():
    bandera = True
    while bandera:
        print("\n--- Eliminar Actor de una Peliculas ---\n")
        peliculas = descargarJson("peliculas")
        print("Seleccione una pelicula:")
        listarIdNomabre()
        idPelicula = input("Seleccione la pelicula por su id: ")
        if idPelicula not in peliculas:
            print(f"No existe una  pelicula con el id {id}")
        else:
            listarActorPelicula(idPelicula)
            idActor = input("Digite el id del actor que va a borrar")
            if idActor not in peliculas[idPelicula]['actores']:
                print("no existe un actor con dicho id")
            else:
                del peliculas[idPelicula]['actores'][idActor]
            guardarJson("peliculas", peliculas)
            print("--- actores eliminado ---")
        bandera = romperCiclo("Quiere eliminar otro actor de está pelicula? ")



def listarIdNomabre():
    peliculas = descargarJson("peliculas")
    print(40 * "-")
    print("ID \t| NOMBRE")
    print(40 * "-")
    for llave, valor in peliculas.items():
        print(f"{llave} \t| {valor['nombre']}")
        print(40 * "-")


def listarActorPelicula(idPelicula):
    peliculas = descargarJson("peliculas")
    for llave, valor in peliculas[idPelicula]["actores"].items():
        print(f"{llave}, nombre: {valor['nombre']}")


def porId():
    peliculas = descargarJson("peliculas")
    id = input("Indique el id de la pelicula: ")
    if id not in peliculas: 
        print("\n--- No existe la pelicula ---\n")
    else:
        print(f"Nombre: {peliculas[id]['nombre']} | Duracion: {peliculas[id]['duracion']} | sinopsis: {peliculas[id]['sinopsis']}")
    salir = input("\nEnter para salir ")


def porNombre():
    peliculas = descargarJson("peliculas")
    nombre = input("Indique el nombre de la pelicula: ").lower()

    for llave, valor in peliculas.items():
        if valor['nombre'] == nombre:
            print(f"Nombre: {peliculas[llave]['nombre']} | Duracion: {peliculas[llave]['duracion']} | sinopsis: {peliculas[llave]['sinopsis']}")
   
    salir = input("\nSi no muestra nada no existe la pelicula.  Enter para salir ")


def listarPeliculas():
    print("--- Listar todas las peliculas ---")
    peliculas = descargarJson("peliculas")
    for llave, valor in peliculas.items():
        print(f"Nombre: {peliculas[llave]['nombre']}  | Duracion: {peliculas[llave]['duracion']} | sinopsis: {peliculas[llave]['sinopsis']}\ngeneros: {[ nombre for nombre in recorrerDiccionario(peliculas[llave]['generos'])]} \nactores: {[ nombre for nombre in recorrerDiccionario(peliculas[llave]['actores'])]}")
    
    salir = input("\nSi no muestra nada no existe la pelicula. Enter para salir ")
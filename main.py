import os
from utils import *
from generos import *
from actores import *
from formatos import *
from peliculas import *


print("Welcome to Blockbuster")
while True:
    print("Menú principal - Sistema gestor de peliculas\n")
    print("\t1.Gestor de genero \n\t2. Gestor de actores \n\t3. Gestor de formatos \n\t4. Gestor de peliculas \n\t5. Gestor de informes\n\t0. Salir\n:")
    opc = input("Seleccione la opcion: ")
    if opc == '1':
        banderag = True
        while banderag:
            os.system("clear")
            print("Gestor de generos\n")
            print("\t1.Crear Genero \n\t2.Listar genero\n:")
            gen = input(": ")
            if gen == '1':
                guardarGenero()
            elif gen == '2':
                listarGeneros()
            else:
                print("La opción ingresada no es valida, intente de nuevo")
            banderag = romperCiclo("Esto va en las funciones")

    elif opc == '2':
        banderaa = True
        while banderaa:
            os.system("clear")
            print("Gestor de actores\n")
            print("\t1.Crear actor \n\t2.Listar actores\n:")
            gen = input(": ")
            if gen == '1':
                guardarActor()
            elif gen == '2':
                listarActores()
            else:
                print("La opción ingresada no es valida, intente de nuevo")
            banderaa = romperCiclo("Esto va en las funciones")
    elif opc == '3':
        banderaf = True
        while banderaf:
            os.system("clear")
            print("Gestor de actores\n")
            print("\t1.Crear formato \n\t2.Listar formatos\n:")
            gen = input(": ")
            if gen == '1':
                guardarFormatos()
            elif gen == '2':
                listarFormatos()
            else:
                print("La opción ingresada no es valida, intente de nuevo")
            banderaf = romperCiclo("Esto va en las funciones")
    elif opc == '4':
        banderap = True
        while banderap:
            os.system("clear")
            print("Gestor de peliculas\n")
            print("\t1.Agregar pelicula \n\t2.Eliminar formatos\n\t3.Eliminar actor de una pelicula\n\t4.Buscar pelicula\n\t5.Listar todas las  pelicula\n:")
            peli = input(": ")
            if peli == '1':
                agregarPelicula()
            elif peli == '2':
                print("Eliminar Peliculas")
                eliminarPelicula()
            elif peli == '3':
                print("Eliminar Actor de una Peliculas")
                eliminarActorDPelicula()
            elif peli == '4':
                print("Buscar pelicula")
                opc = input("\t1.Por id \n\t2.Por nombre\n:")
                if opc == '1':
                    porId()
                elif opc == '2':
                    porNombre()
            elif peli == '5':
                print("Listar todas las peliculas")
                listarPeliculas()

            else:
                print("La opción ingresada no es valida, intente de nuevo")
            banderap = romperCiclo("Esto va en las funciones")
    break
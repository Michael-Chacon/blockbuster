import os
from utils import *
from generos import *
from actores import *
from formatos import *
from peliculas import *


print("Welcome to Blockbuster")
while True:
    os.system("clear")
    print("Menú principal - Sistema gestor de peliculas\n")
    print("\t1. Gestor de genero \n\t2. Gestor de actores \n\t3. Gestor de formatos \n\t4. Gestor de peliculas\n\t0. Salir\n:")
    opc = input("Seleccione la opcion: ")
    if opc == '1':
        banderag = True
        while banderag:
            os.system("clear")
            print("Gestor de generos\n")
            print("\t1.Crear Genero \n\t2.Listar genero\n\t3.Salir")
            gen = input(": ")
            if gen == '1':
                guardarGenero()
                salir = input("enter..")
            elif gen == '2':
                listarGeneros()
                salir = input("enter..")
            elif gen == '3':
                banderag = False
            else:
                salir = input("la opcion no es valida, enter para continuar")


    elif opc == '2':
        banderaa = True
        while banderaa:
            os.system("clear")
            print("Gestor de actores\n")
            print("\t1. Crear actor \n\t2. Listar actores\n\t3. Salir")
            act = input(": ")
            if act == '1':
                guardarActor()
            elif act == '2':
                listarActores()
                salir = input("enter..")
            elif act == '3':
                banderaa = False
            else:
                salir = input("la opcion no es valida, enter para continuar")


    elif opc == '3':
        banderaf = True
        while banderaf:
            os.system("clear")
            print("Gestor de formatos\n")
            print("\t1. Crear formato \n\t2. Listar formatos\n\t3. Salir")
            form = input(": ")
            if form == '1':
                guardarFormatos()
            elif form == '2':
                listarFormatos()
                salir = input("enter..")
            elif form == '3':
                banderaf = False
            else:
                salir = input("la opcion no es valida, enter para continuar")


    elif opc == '4':
        banderap = True
        while banderap:
            os.system("clear")
            print("Gestor de peliculas\n")
            print("\t1. Agregar pelicula \n\t2. Eliminar pelicula\n\t3. Eliminar actor de una pelicula\n\t4. Buscar pelicula\n\t5. Listar todas las  pelicula\n\t6. Salir")
            peli = input(": ")
            if peli == '1':
                agregarPelicula()
            elif peli == '2':
                eliminarPelicula()
            elif peli == '3':
                eliminarActorDPelicula()
            elif peli == '4':
                banderaB = True
                while banderaB:
                    os.system('clear')
                    opc = input("\t1. Por id \n\t2. Por nombre\n\t3. Salir\n:")
                    if opc == '1':
                        porId()
                    elif opc == '2':
                        porNombre()
                    elif opc == '3':
                        banderaB = False
                    else:
                        salir = input("Opcion incorrecta, enter para continuar")
            elif peli == '5':
                listarPeliculas()
            elif peli == '6':
               banderap = False
            else:
                print("La opción ingresada no es valida, intente de nuevo")
                salir = input("Opcion incorrecta, enter para continuar")

    elif opc == '0':
        break
    else: 
       salir =  input("Opcion incorrecta, enter para intentar de nuevo")

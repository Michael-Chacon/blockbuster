import os
from generos import *
from actores import *
from utils import *
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
    break
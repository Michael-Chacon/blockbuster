import os 
from conexion import descargarJson
from utils import recorrerDiccionario
from generos import listarGeneros


def pelisPorGenero():
    os.system('clear')
    generos = descargarJson("generos")
    peliculas = descargarJson("peliculas")

    print("\n--- Buscar peliculas por genero ---\n")
    listarGeneros()
    idGernero = input("\nIngrese el id del genero: ")

    if idGernero not in generos:
        print(f"\n-- Error - No existe un genero con el id {idGernero} --\n")
    else:
        print(f"Has selecciconado el genero {generos[idGernero]['nombre'].title()}")
        cont = 0
        for id, datos in peliculas.items():
            if idGernero not in datos['generos']:
                continue
            else:
                cont += 1
                print(60 * '-')
                print(f"\t{peliculas[id]['nombre'].upper()}")
                print("")
                print(f"Duracion: {peliculas[id]['duracion']} min. | sinopsis: {peliculas[id]['sinopsis']}")
                print("Actores:")
                for nombre in recorrerDiccionario(peliculas[id]['actores']):
                    print(f"\t- {nombre.title()}")
                print(60 * '-')
        if cont == 0:
            print(f"\n*** No hay pelicula del genero {generos[idGernero]['nombre'].title()} ***\n")
        input("Enter para salir...")

def Stallone():
    os.system('clear')
    peliculas = descargarJson("peliculas")
    print("\n--- Peliculas donde el prota sea Silvester Stallone ---\n")
    cont = 0
    for id, _ in peliculas.items():
        for _, nombres in peliculas[id]['actores'].items():
            if "Silvester Stallone" not in nombres['nombre']:
                continue
            else:
                cont += 1
                print(60 * '-')
                print(f"\t{peliculas[id]['nombre'].upper()}")
                print("")
                print(f"Duracion: {peliculas[id]['duracion']} min. | sinopsis: {peliculas[id]['sinopsis']}")
                print("Generos:")
                for nombre in recorrerDiccionario(peliculas[id]['generos']):
                    print(f"\t- {nombre.title()}")
                print("Actores:")
                for nombre in recorrerDiccionario(peliculas[id]['actores']):
                    print(f"\t- {nombre.title()}")
                print(60 * '-')
    if cont == 0:
        print(f"\n*** No hay pelicula donde Silvester Stallone actue ***\n")
    input("Enter para salir...")

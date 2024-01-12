from conexion import descargarJson


def romperCiclo(mensaje):
    print(f"\n{mensaje} \n\ts: si\n\tn: no\n")
    opcion = input("")
    if opcion == 'n':
        return False
    else: 
        return True
        

def generarId(archivo):
    modulo = descargarJson(archivo)
    if len(modulo) == 0:
        id = 1
    else:
        idDiccionario = list(modulo.keys())[-1]
        id = int(idDiccionario) + 1
        print(id)
    return id


def validar(tipo):
    while True:
        campo = input(": ")
        if tipo == int:
            if campo.isdigit():
                return campo
            else:
                print("tipo de dato incorrecto, ingrese un número entero")
        elif tipo == str:
            palabras = campo
            campo = campo.replace(" ","")
            if campo.isalpha():
                return palabras
            else:
                print("tipo de dato incorrecto, ingrese un texto")
        elif tipo == float:
            if not campo.isalpha():
                try:
                    campo = float(campo)
                    return campo
                except:
                    print("tipo de dato incorrecto, ingrese un decimal (.)")
            else:
                print("tipo de dato incorrecto, ingrese un decimal (.)")
        else:
                print("tipo de dato incorrecto, ingrese el dato nuevamente")

def recorrerDiccionario(generos):
    arr = []
    for llave, valor in generos.items():
        arr.append(valor['nombre'])
    return arr

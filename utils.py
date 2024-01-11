from conexion import descargarJson
def romperCiclo(mensaje):
    print(f"{mensaje} \n\ts: si\n\tn: no")
    opcion = input(": ")
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
    return id;

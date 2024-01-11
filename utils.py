
def romperCiclo(mensaje):
    print(f"{mensaje} \n\ts: si\n\tn: no")
    opcion = input(": ")
    if opcion == 'n':
        return False
    else: 
        return True
        

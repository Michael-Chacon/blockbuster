
def romperCiclo(mensaje):
    print(f"{mensaje} \n\ts: si\n\tn: no")
    opcion = input(": ")
    if opcion == 'n':
        return False
    elif opcion != 's' and opcion != 'n':
        print("Error opcion incorrecta: Enter para continuar")
        return True
        

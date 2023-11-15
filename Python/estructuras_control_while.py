seguir_preguntando = True

while seguir_preguntando:
    numero = int(input("por favor ingrese un numero entre 1 y 10: "))

    if 1 <= numero <= 10:
        seguir_preguntando = False

    else:
        print("Por favor ingrese un numero valido")


print("ADIOS")

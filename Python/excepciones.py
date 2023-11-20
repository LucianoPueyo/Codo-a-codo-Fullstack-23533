# Manejo de excepciones

def validar_input():
    continuar = True

    while continuar:
        try:
            resultado = int(input("Ingrese un numero: "))
            continuar = False

        except ValueError as ve:
            print("Por favor solo ingresar numeros enteros(sin coma decimal)", str(ve))

    return resultado

def validar_input_distinto_0():
    continuar = True

    while continuar:
        try:
            resultado = int(input("Ingrese un numero: "))
            if(resultado == 0):
                raise AssertionError("El valor no puede ser 0")
            continuar = False

        except ValueError as ve:
            print("Por favor solo ingresar numeros enteros(sin coma decimal)", str(ve))

        except AssertionError as ae:
            print(str(ae))

    return resultado


dividendo = validar_input()
divisor = validar_input_distinto_0()

print(f"{dividendo}/{divisor} = {dividendo / divisor}")


"""
print("DIVISION 2.0")
try:
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro: "))

    print(a / b)

except ValueError as ve:
    print("Por favor solo ingresar numeros enteros(sin coma decimal)", str(ve))

except ZeroDivisionError as zde:
    print("El divisor no puede ser 0", str(zde))


"""
print("ADIOS")
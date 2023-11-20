# Parametros Posicionales Obligatorios
def funcion_1(a, b):
    print(a / b)

funcion_1(4, 2)
funcion_1(2, 4)

# funcion_1(5) ! La funcion espera recibir dos valores, como solo le paso 1, me da error.

# Parametros opcionales
def funcion_2(a, b=0):
    print(a, b)

funcion_2(8, 10)
funcion_2("hola")

# Parametros por nombre
def funcion_3(suma, promedio):
    print(f"La suma es {suma} y el promedio total es {promedio}")

funcion_3(suma=5.0, promedio=10.0)
funcion_3(promedio=10.0, suma=5.0)
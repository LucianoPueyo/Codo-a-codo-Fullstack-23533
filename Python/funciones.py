# Definicion
def suma(a, b):
    return a + b

def saludar():
    print("Bienvenido")

# Funcion vacia
def promedio_curso(lista):
    pass

def saludar_nombre(nombre):
    return f"Hola {nombre}"


print(suma(8, 10))
print(suma("Hola", " Mundo funciones"))

saludar()


notas = [6,7,8,10,9,5]
promedio_curso(notas)

print(saludar_nombre("Carlos"))
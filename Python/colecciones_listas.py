# Listas

# Crear
#        0        1     2     3
#        -4      -3    -2    -1
lista1 = ["Hola", "Si", "No", "Adios"]

# Ver contenido
print(lista1[0])
print(lista1[len(lista1) - 1]) # Ultimo elemento
print(lista1[-1]) # Ultimo elemento
print(lista1)

# Modificarlo
lista1[0] = "Telefono"
print(lista1)

# Agregar elementos
lista1.append("Video")
print(lista1)

# Quitar elementos
valor = lista1.pop()
print(valor, lista1)

print("------------------------------------")
# iterar
# for clasico
for i in range(0, len(lista1)):
    print(lista1[i])

print("------------------------------------")
# foreach
for palabra in lista1:
    print(palabra)

print("------------------------------------")
# Operaciones comunes

# Ordenar
numeros = [9,1,8,2,7,3,4,6,5,0]

print(numeros)

numeros.sort()

print(numeros)

# Pertenencia
print("Caballo" in lista1)
print("Telefono" in lista1)


# Max y Min
print(max(numeros), min(numeros), sum(numeros))
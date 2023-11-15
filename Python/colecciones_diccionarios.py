#Diccionarios

# Pares clave-valor
diccionario1 = {
    'Pedro': 10,
    'Maria': 9,
    'Carlos': 7,
    'Sofia': 8
}

# Agregar un elemento
print(diccionario1)
diccionario1['Lucio'] = 5
print(diccionario1)

# Modificar un valor
diccionario1['Lucio'] = 8
print(diccionario1)


# Acceso a un valor
print(diccionario1['Pedro'])

# Iterando
print("For each:")
for clave in diccionario1:
    print(clave, diccionario1[clave])

print("Solo valores")
for valor in diccionario1.values():
    print(valor)

print("Solo claves")
for valor in diccionario1.keys():
    print(valor)

print("Itero sobre los items (clave, valor)")
for clave, valor in diccionario1.items():
    print(clave, valor)

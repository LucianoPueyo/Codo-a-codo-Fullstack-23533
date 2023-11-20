# Las funciones lambda son funciones anonimas
lista_numeros = [1,2,3,4,5,6]

# Obtener los cuadrados de una lista de numeros
cuadrados = []
for numero in lista_numeros:
    cuadrados.append(numero ** 2)

print(cuadrados)

resultado = map(lambda numero : numero ** 2, lista_numeros)
print(list(resultado))

# Filtrar palabras de mas de tres caracteres
lista_palabras = ["Hola", "Si", "No", "Divisible", "Tomas", "Bis", "Yes"]

# Usando un for comun y corriente
palabras_filtradas = []

for palabra in lista_palabras:
    if len(palabra) > 3:
        palabras_filtradas.append(palabra)

print(palabras_filtradas)

# Lo mismo pero con funciones lambda:
palabras_filtradas = filter(lambda palabra : len(palabra) > 3, lista_palabras)

print(list(palabras_filtradas))
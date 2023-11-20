# Pasaje por referencia
def agregar_valor(lista, valor):
    lista.append(valor)


mi_lista = [1,2,3,4]

print(mi_lista)

agregar_valor(mi_lista, 5)

print(mi_lista)


def obtener_lista_ordenada_menor_a_mayor(parametro_lista):
    copia = parametro_lista[:] # Slice | esto es una copia independiente
    copia.sort()

    return copia

lista2 = [8,7,1,5,9]

resultado = obtener_lista_ordenada_menor_a_mayor(lista2)

print("Lista original", lista2)
print("lista ordenada", resultado)

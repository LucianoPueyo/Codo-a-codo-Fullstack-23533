def es_par(numero):
    return numero % 2 == 0

print(es_par(8))
print(es_par(9))


def sumatoria(lista_notas):
    suma = 0
    for nota in lista_notas:
        suma += nota

    return suma

def promedio(lista_notas):
    return sumatoria(lista_notas) / len(lista_notas)


def calcular_suma_promedio(lista_notas):
    return sumatoria(lista_notas), promedio(lista_notas)
    

notas = [10,7,8,9,5]
print(calcular_suma_promedio(notas))
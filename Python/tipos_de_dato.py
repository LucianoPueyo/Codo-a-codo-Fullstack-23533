"""
    Tipos básicos
    int     (numeros enteros)
    float   (numeros de coma flotante)
    complex (numeros complejos)
    bool    (booleanos)
    str  (cadenas de texto)
"""

suma = 2 + 2
print(suma)

suma = "2" + "2"
print(suma)

# No puedo sumar strings y enteros
# Por lo tanto ambos opreandos deben ser de igual tipo
suma = "2" + str(2)
print(suma)

suma = int("2") + 2
print(suma)

suma = 2 + 3.14
print(suma)
a = 5 # Global

# Los Scopes(Ambitos) Locales pueden ver hacia afuera(Scope Global) 

def funcion():
    # Scope Local
    print(a)

funcion()

# Los Scopes Globales no pueden ver los scopes locales
def funcion2():
    b = 20 # Local
    print("Print interno de la funcion2: ", b)


funcion2()
# print(b) # Al intentar hacer un print de una variable local en el scope externo, me da error


# Ojo en este ejemplo, lo que tenemos es dos variables distintas, definidas en dos namespaces distintos.
# Si bien su nombre coincide, realmente son espacios de memoria distintos.

# Por lo tanto, lo mejor que podemos hacer, es evitar caer en estos casos.
# Una forma facil de identificar a las variables globales es usuando la convencion de nombres para dichos casos:

# NOMBRE_DE_VARIABLE_GLOBAL = 10

c = 3

def funcion3():
    c = 5
    print(c)

funcion3()
print(c)
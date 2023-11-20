class Alumno:
    def __init__(self, nombre, apellido, legajo):
        """
            En python, todos los metodos y atributos son publicos.

            A su vez en Python, podemos hacer que los atributos sean "privados".

            En python, anteponer dos guiones bajos a un nombre de atributo se lo conoce como mangling.
        """
        self.__nombre = nombre
        self.__apellido = apellido
        self.__legajo = legajo

    # Getters y setters
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def legajo(self):
        return self.__legajo
    
    def __str__(self):
        return f'{self.__nombre} {self.__apellido} {self.__legajo}'


alumno1 = Alumno('Carlos', 'Lopez', 'A-00001234')
alumno2 = Alumno('Maria', 'Del Cerro', 'A-00005678')


print(alumno1.nombre)
alumno1.nombre = "Gaston"
print(str(alumno1))

print(alumno1.legajo)
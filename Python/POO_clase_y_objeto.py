class Persona:
    def __init__(self, nombre, apellido, edad, dni):
        """
            El metodo __init__ es un metodo especial. En particular el init es el constructor de una clase.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def presentar(self):
        print(f"Nombre completo: {self.nombre} {self.apellido} Edad: {self.edad} dni: {self.dni}")

    def caminar(self):
        print("Estoy caminando")

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.edad} - {self.dni}"


persona1 = Persona('Carlos', 'Lopez', 25, 1234) # Instanciar la clase Persona
persona2 = Persona(
    nombre= 'Maria',
    apellido= 'Del Cerro',
    edad= 30,
    dni= 4567
)

persona3 = Persona('Gaston', 'Perez', 35, 1111)

# Accediendo a atributos puntuales
print(persona1.nombre, persona1.apellido, persona1.edad, persona1.dni)
print(persona2.nombre)

# Invocando un metodo
persona1.presentar()
persona2.presentar()

persona1.caminar()
persona2.caminar()


lista_personas = [
    persona1,
    persona2,
    persona3,
]

for persona in lista_personas:
    persona.presentar()

print("-----------------------------------------------------")
persona1.presentar()
persona1.edad = 55
persona1.presentar()

lista = [1,2,3]
print(lista)

print(persona1)
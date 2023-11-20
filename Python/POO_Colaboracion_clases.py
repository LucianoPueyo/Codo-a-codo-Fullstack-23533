class Alumno:
    max_cantidad_cursos = 3 # Atributo de clase

    def __init__(self, nombre, apellido, dni, legajo):
        self.nombre = nombre # Atributos de Instancia
        self.apellido = apellido
        self.dni = dni
        self.legajo = legajo

    def __mostrar(self):
        return f'{self.nombre} {self.apellido} {self.legajo}'

    def __str__(self):
        return self.__mostrar()

    def __repr__(self):
        return self.__mostrar()


class Docente:
    def __init__(self, nombre, apellido, dni, cuit):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cuit = cuit

    def __mostrar(self):
        return f'{self.nombre} {self.apellido} {self.cuit}'

    def __str__(self):
        return self.__mostrar()

    def __repr__(self):
        return self.__mostrar()

class Curso:
    def __init__(self, nombre, descripcion, cupos):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cupos = cupos
        self.alumnos_listado = []
        self.docente = None

    def agregar_alumno(self, alumno):
        if len(self.alumnos_listado) < self.cupos:
            self.alumnos_listado.append(alumno)

        else:
            print(f'Este curso está lleno! el alumno: {alumno} no pudo ser inscripto.')

    def agregar_docente(self, docente):
        if self.docente:
            print("No se puede inscribir mas de un docente")

        else:
            self.docente = docente

    def __str__(self):
        docente = str(self.docente) if self.docente is not None else 'Sin docente asignado' # If ternario
        return f'{self.nombre} Alumnos inscriptos: {len(self.alumnos_listado)} / cupos: {self.cupos} - Docente asignado: {docente}' 


alumno1 = Alumno('Carlos', 'Lopez', 1234, 'A-00001234')
alumno2 = Alumno('Maria', 'Del Cerro', 5678, 'A-00005678')
alumno3 = Alumno('Gaston', 'Perez', 9012, 'A-00009012')
alumno4 = Alumno('Carina', 'Gomez', 5555, 'A-00005555')

docente1 = Docente('Pedro', 'Torres', 8677, '30-8677-1')
docente2 = Docente('Lucia', 'Mendez', 1236, '36-1236-1')

curso1 = Curso(
    nombre='Python Fullstack', 
    descripcion='Este es un curso de introducción a la programación frontend y backend con python',
    cupos=3
)

print(curso1)

curso1.agregar_alumno(alumno1)
curso1.agregar_alumno(alumno2)
curso1.agregar_alumno(alumno3)
curso1.agregar_alumno(alumno4)

print(curso1)

curso1.agregar_docente(docente1)
curso1.agregar_docente(docente2)
print(curso1)

print(Alumno.max_cantidad_cursos)
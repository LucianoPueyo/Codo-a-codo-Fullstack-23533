class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def mostrar(self):
        return f'{self.nombre} {self.apellido} {self.dni}'

    def __str__(self):
        return self.mostrar()

    def __repr__(self):
        return self.mostrar()


class Alumno(Persona):
    max_cantidad_cursos = 3 # Atributo de clase

    def __init__(self, nombre, apellido, dni, legajo):
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo

    def mostrar(self):
        mensaje = super().mostrar()
        return f'{mensaje} {self.legajo}'


class Docente(Persona):
    def __init__(self, nombre, apellido, dni, cuit):
        super().__init__(nombre, apellido, dni)
        self.cuit = cuit

    def mostrar(self):
        mensaje = super().mostrar()
        return f'{mensaje} {self.cuit}'


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
docente1 = Docente('Pedro', 'Torres', 8677, '30-8677-1')
curso1 = Curso(
    nombre='Python Fullstack', 
    descripcion='Este es un curso de introducción a la programación frontend y backend con python',
    cupos=3
)
print(alumno1) # invoco al __str__()
print(docente1)

curso1.agregar_alumno(alumno1)
curso1.agregar_docente(docente1)

print(curso1)
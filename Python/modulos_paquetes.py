from POO_Herencia import Alumno, Docente, Curso


alumno_1 = Alumno('Carlos', 'Lopez', 1531, 'A-00001531')

curso_1 = Curso('Fullstack Java', 'Un curso de fullstack con backend de Java', 10)

curso_1.agregar_alumno(alumno_1)

print(curso_1)
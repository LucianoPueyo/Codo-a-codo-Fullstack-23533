a = 30
b = 30
c = True

if a > b:
    print("A es mayor que B")

elif a < b:
    print("A es menor que B")

else:
    print("A y B son iguales")

print("Aprueba el alumno Codo a Codo?")

efi = bool(int(input("Aprobó el EFI?(1/0) ")))
asistencia =bool(int(input("Tiene 60 o mas de asistencia?(1/0) ")))

if efi and asistencia:
    print("El alumno aprueba")

else:
    print("El alumno no aprueba")

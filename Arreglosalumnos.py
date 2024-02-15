import random

class Alumno:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

class Materia:
    def __init__(self, nombre):
        self.nombre = nombre

alumnos = [
    Alumno("Alumno {}".format(i), [0] * 6) for i in range(1, 101)
]

materias = [Materia("Materia {}".format(i)) for i in range(1, 7)]

for alumno in alumnos:
    for i in range(6):
        alumno.calificaciones[i] = random.randint(1, 100)

print("Tabla de Calificaciones:")
print("Alumno\t\t\tMateria 1\tMateria 2\tMateria 3\tMateria 4\tMateria 5\tMateria 6")
for alumno in alumnos:
    print(f"{alumno.nombre}\t\t{alumno.calificaciones[0]}\t\t{alumno.calificaciones[1]}\t\t{alumno.calificaciones[2]}\t\t{alumno.calificaciones[3]}\t\t{alumno.calificaciones[4]}\t\t{alumno.calificaciones[5]}")

while True:
    alumno_buscar = input("Ingrese el número de alumno que desea buscar (1-100), o 'exit' para salir: ")
    if alumno_buscar.lower() == 'exit':
        break
    try:
        num_alumno = int(alumno_buscar)
        if num_alumno < 1 or num_alumno > 100:
            print("Número de alumno fuera de rango. Por favor, ingrese un número entre 1 y 100.")
            continue
        alumno = alumnos[num_alumno - 1]
        print(f"\nAlumno: {alumno.nombre}")
        print("Calificaciones:")
        for i, calificacion in enumerate(alumno.calificaciones):
            print(f"Materia {i+1}: {calificacion}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido o 'exit' para salir.")


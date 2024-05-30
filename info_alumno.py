#8.	Crea un programa que almacene información sobre alumnos utilizando tuplas. Cada tupla debe contener
# el nombre, la edad y el promedio de calificaciones de un alumno. Luego, puedes realizar operaciones como
# buscar el alumno con el promedio más alto.

# Almacenamos información sobre tres alumnos
alumnos = (
    ("Alumno 1", 18, 8.5),
    ("Alumno 2", 19, 7.8),
    ("Alumno 3", 20, 9.2)
)

# Función para buscar el alumno con el promedio más alto
def alumno_con_promedio_mas_alto(alumnos):
    # Suponemos que el primer alumno tiene el promedio más alto
    alumno_con_promedio_mas_alto = alumnos[0]

    # Recorremos el resto de los alumnos
    for alumno in alumnos[1:]:
        # Si el promedio de este alumno es más alto que el promedio del alumno actual
        if alumno[2] > alumno_con_promedio_mas_alto[2]:
            # Actualizamos el alumno con el promedio más alto
            alumno_con_promedio_mas_alto = alumno

    # Devolvemos el alumno con el promedio más alto
    return alumno_con_promedio_mas_alto

# Buscamos el alumno con el promedio más alto
alumno_mas_alto = alumno_con_promedio_mas_alto(alumnos)

print("El alumno con el promedio más alto es:", alumno_mas_alto[0])
print("Su edad es:", alumno_mas_alto[1])
print("Su promedio es:", alumno_mas_alto[2])
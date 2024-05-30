#1.	Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que  introduzca el
# nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un
# asterisco (*) Al finalizar se mostrará los siguientes datos:
#Todos los estudiantes mayores de edad.
#Los alumnos mayores (los que tienen más edad)

# Creamos un diccionario vacío para guardar los nombres y edades de los alumnos
alumnos = {}

while True:
    # Pedimos al usuario que ingrese el nombre y la edad
    nombre = input("Ingrese el nombre del alumno (ingrese * para terminar): ")
    if nombre == "*":
        # Si el nombre es *, terminamos el bucle
        break
    edad = int(input("Ingrese la edad del alumno: "))

    # Agregamos el nombre y la edad al diccionario
    alumnos[nombre] = edad

# Mostramos los estudiantes mayores de edad
print("\nEstudiantes mayores de edad:")
for nombre, edad in alumnos.items():
    if edad >= 18:
        print(f"- {nombre} ({edad} años)")

# Calculamos los alumnos mayores
mayores = max(alumnos, key=alumnos.get)
print(f"\nEl alumno mayor es: {mayores} ({alumnos[mayores]} años)")

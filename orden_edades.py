#4.	Realizar un programa que permite recolectar edades y luego organizar de menor a mayor use (listas o tuplas)

# Creamos una lista vacía para almacenar las edades
edades = []

# Pedimos al usuario que ingrese las edades
while True:
    edad = input("Ingrese una edad (o 'fin' para terminar): ")
    if edad.lower() == 'fin':
        break
    try:
        edad = int(edad)
        edades.append(edad)
    except ValueError:
        print("Error: la edad debe ser un número entero")

# Organizamos las edades de menor a mayor
edades.sort()

# Mostramos las edades organizadas
print("Edades organizadas de menor a mayor:")
for edad in edades:
    print(edad)
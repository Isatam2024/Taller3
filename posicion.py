#3.	Buscar un elemento dentro de una lista que nosotros le pedimos por teclado.
# Indicar la posición donde se encuentra. Si hay más de uno, indicar igualmente la posición.
# Solicitar una lista de elementos al usuario
elementos = input("Ingrese una lista de elementos separados por espacios: ").split()

# Solicitar el elemento a buscar
elemento_a_buscar = input("Ingrese el elemento que desea buscar: ")

# Encontrar las posiciones del elemento en la lista
posiciones = [i for i, elemento in enumerate(elementos) if elemento == elemento_a_buscar]

# Mostrar el resultado
if not posiciones:
    print("El elemento no se encuentra en la lista.")
else:
    print(f"El elemento {elemento_a_buscar} se encuentra en la posición: {posiciones}")
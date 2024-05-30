#1.	Desarrolle un algoritmo que lea una cédula y la busque en una lista de X posiciones donde se encuentran
# los documentos de identidad de las personas que pueden votar para elecciones de presidente en el presente año.
# Imprima si puede votar o no. Hacer este ejercicio con método de búsqueda secuencial

def buscar_cedula(cedula, lista_documentos):
    encontrado = False
    for i in range(len(lista_documentos)):
        if lista_documentos[i] == cedula:
            encontrado = True
            break
    if encontrado:
        print("La cédula", cedula, "se encuentra en la lista de documentos de identidad. Puede votar.")
    else:
        print("La cédula", cedula, "no se encuentra en la lista de documentos de identidad. No puede votar.")

# Ejemplo de lista de documentos de identidad
lista_documentos = ["12345678", "23456789", "34567890", "45678901", "56789012"]

# Ingrese la cédula a buscar
cedula = input("Ingrese la cédula a buscar: ")

# Buscar la cédula en la lista
buscar_cedula(cedula, lista_documentos)
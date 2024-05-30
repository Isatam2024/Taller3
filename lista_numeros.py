#Crear una lista con n números, ingresados por teclado y mostrar sus valores elevados al cuadrado.
lista = []

for i in range (10) :
    Numero= int(input("Ingresar el número que desea elevar al cuadrado:"))
    lista.append(Numero)
    print(lista[i]**2)


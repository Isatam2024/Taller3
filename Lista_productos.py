# Diseñe una lista en el que se ingrese la cantidad de productos y sus respectivos precios, para la preparación de un
# plato, también se debe mostrar al final el costo a gastar.


cantidad_productos = int(input("Ingrese la cantidad de productos que necesita para preparar el plato: "))

productos = []

for i in range(cantidad_productos):
    nombre_producto = input("Ingrese el nombre del producto {}: ".format(i+1))
    precio_producto = float(input("Ingrese el precio del producto {}: ".format(i+1)))
    productos.append((nombre_producto, precio_producto))

costo_total = sum(precio for _, precio in productos)

print("\nLista de productos y precios:")
for producto in productos:
    nombre, precio = producto
    print(nombre, "- Precio:", precio)

print("\nCosto total a gastar:", costo_total)
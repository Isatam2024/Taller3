#4.	Diseñar un programa que guarde en un diccionario los precios de productos, pregunte al usuario por un producto,
# un número de productos y muestre por pantalla el precio de ese número de productos. Si el producto no está en el diccionario
# debe mostrar un mensaje informando de ello.

import tkinter as tk

# Creamos un diccionario con los precios de los productos
precios = {
    "manzana": 1.50,
    "pera": 2.00,
    "naranja": 1.20,
    "plátano": 0.80,
    "fresa": 3.00
}

def mostrar_precio():
    # Pedimos al usuario que ingrese el producto y la cantidad
    producto = entrada_producto.get()
    cantidad = int(entrada_cantidad.get())

    # Verificamos si el producto está en el diccionario
    if producto in precios:
        # Calculamos el precio total
        precio_total = precios[producto] * cantidad
        label_resultado.config(text=f"El precio de {cantidad} {producto}(s) es de ${precio_total:.2f}")
    else:
        label_resultado.config(text="Lo siento, no tenemos ese producto en nuestra lista.")

# Creamos la ventana tkinter
ventana = tk.Tk()
ventana.title("Precio de productos")

# Creamos las etiquetas y entradas para el producto y la cantidad
label_producto = tk.Label(ventana, text="Producto:")
label_producto.pack()
entrada_producto = tk.Entry(ventana)
entrada_producto.pack()

label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.pack()
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.pack()

# Creamos el botón para calcular el precio
boton_calcular = tk.Button(ventana, text="Calcular precio", command=mostrar_precio)
boton_calcular.pack()

# Creamos la etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Iniciamos la ventana
ventana.mainloop()
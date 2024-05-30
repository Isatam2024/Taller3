#2.	Diseñar un programa que cree un diccionario simulando un carrito de las compras. El programa debe preguntar
# el artículo y su precio y añadir al diccionario, hasta que el usuario
# decida hacer el pago. Después se debe mostrar por pantalla la lista de la compra y el total a pagar, con el siguiente formato


import tkinter as tk

class Carrito:
    def __init__(self):
        self.carrito = {}

    def agregar_producto(self, articulo, precio):
        self.carrito[articulo] = precio

    def mostrar_carrito(self):
        total = 0
        lista_productos = ""
        for articulo, precio in self.carrito.items():
            lista_productos += f"{articulo}: ${precio}\n"
            total += precio
        return lista_productos, total

class VentanaCarrito(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Carrito de compras")
        self.carrito = Carrito()

        self.label_articulo = tk.Label(self, text="Artículo:")
        self.label_articulo.grid(row=0, column=0)
        self.entry_articulo = tk.Entry(self)
        self.entry_articulo.grid(row=0, column=1)

        self.label_precio = tk.Label(self, text="Precio:")
        self.label_precio.grid(row=1, column=0)
        self.entry_precio = tk.Entry(self)
        self.entry_precio.grid(row=1, column=1)

        self.boton_agregar = tk.Button(self, text="Agregar producto", command=self.agregar_producto)
        self.boton_agregar.grid(row=2, column=0, columnspan=2)

        self.label_lista_productos = tk.Label(self, text="Lista de productos:")
        self.label_lista_productos.grid(row=3, column=0, columnspan=2)
        self.text_lista_productos = tk.Text(self, width=40, height=10)
        self.text_lista_productos.grid(row=4, column=0, columnspan=2)

        self.label_total = tk.Label(self, text="Total a pagar:")
        self.label_total.grid(row=5, column=0)
        self.label_total_valor = tk.Label(self, text="")
        self.label_total_valor.grid(row=5, column=1)

    def agregar_producto(self):
        articulo = self.entry_articulo.get()
        precio = float(self.entry_precio.get())
        self.carrito.agregar_producto(articulo, precio)
        self.mostrar_carrito()

    def mostrar_carrito(self):
        lista_productos, total = self.carrito.mostrar_carrito()
        self.text_lista_productos.delete(1.0, tk.END)
        self.text_lista_productos.insert(tk.END, lista_productos)
        self.label_total_valor.config(text=f"${total:.2f}")

ventana = VentanaCarrito()
ventana.mainloop()
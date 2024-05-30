#3.	Diseñar un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
# mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes
# notas introducidas por el usuario.

import tkinter as tk

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

def mostrar_notas():
    texto = ""
    for i in range(len(asignaturas)):
        texto += f"En {asignaturas[i]} has sacado {notas[i]}\n"
    label.config(text=texto)

def agregar_notas():
    for asignatura in asignaturas:
        nota = float(input(f"Introduce la nota de {asignatura}: "))
        notas.append(nota)
    ventana = tk.Tk()
    ventana.title("Notas")
    global label
    label = tk.Label(ventana, text="", wraplength=400)
    label.pack()
    mostrar_notas()
    ventana.mainloop()

agregar_notas()
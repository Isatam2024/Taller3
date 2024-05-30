#2.	Hacer un programa que inicialice una lista de números con valores aleatorios, y posterior
# ordene los elementos de menor a mayor.

import random

# Generamos una lista de 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]

# Ordenamos la lista de menor a mayor
numeros.sort()

# Imprimimos la lista ordenada
print(numeros)
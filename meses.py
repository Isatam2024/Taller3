#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30)
# y el nombre del mes. Debes usar una lista.
# Para simplificarlo vamos a suponer que febrero tiene 28 días

# Definimos una lista de meses con sus nombres y el número de días
meses = [
    {"nombre": "enero", "dias": 31},
    {"nombre": "febrero", "dias": 28},
    {"nombre": "marzo", "dias": 31},
    {"nombre": "abril", "dias": 30},
    {"nombre": "mayo", "dias": 31},
    {"nombre": "junio", "dias": 30},
    {"nombre": "julio", "dias": 31},
    {"nombre": "agosto", "dias": 31},
    {"nombre": "septiembre", "dias": 30},
    {"nombre": "octubre", "dias": 31},
    {"nombre": "noviembre", "dias": 30},
    {"nombre": "diciembre", "dias": 31},
]

# Pedimos al usuario que ingrese un número de mes
numero_mes = int(input("Ingrese el número de un mes (1-12): "))

# Verificamos que el número de mes sea válido
if 1 <= numero_mes <= 12:
    # Buscamos el mes en la lista de meses
    mes = next((m for m in meses if m["nombre"] == ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"][numero_mes-1]), None)
    if mes:
        print(f"El mes {numero_mes} es {mes['nombre']} y tiene {mes['dias']} días.")
    else:
        print("No se encontró el mes")
else:
    print("El número de mes debe ser un valor entre 1 y 12.")
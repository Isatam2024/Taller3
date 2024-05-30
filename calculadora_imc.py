#Calculadora IMC

# Función para calcular el IMC
def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

# Pedir al usuario que ingrese su peso y estatura
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, estatura)

# Mostrar el resultado
print(f"Su IMC es: {imc:.2f}")

# Agregar la lógica para interpretar el IMC
if imc < 18.5:
    print("Esta por debajo del peso normal.")
elif imc <= 24.9:
    print("Esta en su peso normal.")
elif imc <= 29.9:
    print("Esta en sobrepeso.")
elif imc <= 34.9:
    print("Esta en obesidad grado I.")
elif imc <= 39.9:
    print("Esta en obesidad grado II.")
else:
    print("Esta en obesidad grado III.")
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))

IMC = peso / (altura * altura)

if IMC > 0 and IMC < 16:
    diagnostico = "Criterio de ingreso en hospital"
elif IMC >= 16 and IMC <= 17:
    diagnostico = "Infrapeso"
elif IMC > 17 and IMC <= 18:
    diagnostico = "Bajo peso"
elif IMC > 18 and IMC <= 25:
    diagnostico = "Peso normal (saludable)"
elif IMC > 25 and IMC <= 30:
    diagnostico = "Sobrepeso (obsesidad de grado I)"
elif IMC > 30 and IMC <= 35:
    diagnostico = "Sobrepeso cronico (obsesidad de grado II)"
elif IMC > 35 and IMC <= 40:
    diagnostico = "Sobrepeso premorbida (obsesidad de grado III)"
elif IMC > 40:
    diagnostico = "Sobrepeso morbida (obsesidad de grado IV)"
else:
    diagnostico = "No es posible encontrar informacion"

print("Si indice de masa corporal es: ", IMC,
      "y su diagnostico es: ", diagnostico)

input()
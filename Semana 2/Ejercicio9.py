personas_captura = int(input("¿Cuantas personas desea capturar? :"))
lista_personas = []

for contador in range(0, personas_captura):
    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))
    IMC = peso / (altura * altura)
    lista_personas.append(IMC)

for contador in range(0, personas_captura):
    IMC = lista_personas[contador]
    if IMC > 0 and IMC < 16:
        print("Persona # ", contador+1, "Criterio de ingreso en hospital")
    elif IMC >= 16 and IMC <= 17:
        print("Persona # ", contador+1, "Infrapeso")
    elif IMC > 17 and IMC <= 18:
        print("Persona # ", contador+1, "Bajo peso")
    elif IMC > 18 and IMC <= 25:
        print("Persona # ", contador+1, "Peso normal (saludable)")
    elif IMC > 25 and IMC <= 30:
        print("Persona # ", contador+1, "Sobrepeso (obsesidad de grado I)")
    elif IMC > 30 and IMC <= 35:
        print("Persona # ", contador+1,
              "Sobrepeso cronico (obsesidad de grado II)")
    elif IMC > 35 and IMC <= 40:
        print("Persona # ", contador+1,
              "Sobrepeso premorbida (obsesidad de grado III)")
    elif IMC > 40:
        print("Persona # ", contador, "Sobrepeso morbida (obsesidad de grado IV)")
    else:
        print("No es posible encontrar informacion")

print(lista_personas)

input()

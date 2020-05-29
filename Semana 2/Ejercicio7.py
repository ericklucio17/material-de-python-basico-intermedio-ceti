import random

numero_ganador = random.randint(1, 50)

print("Estoy pensando un numero entre 1 y 50")

inferior = 1
superior = 50

for intentos in range (1, 6):
    captura = int(input("Ingrese un numero: "))
    if captura == numero_ganador:
        print("Felicidades, adivinaste el numero")
        break
    elif captura < numero_ganador:
        inferior = captura 
        print("El numero esta entre ",inferior, " y ", superior)
    elif captura > numero_ganador:
        superior = captura
        print("El numero esta entre ",inferior, " y ", superior)

print("Se acabaron los intentos, el numero que pense era ", numero_ganador)

input()
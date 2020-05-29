l1 = float(input("Ingrese el lado 1 de un triangulo: "))
l2 = float(input("Ingrese el lado 2 de un triangulo: "))
l3 = float(input("Ingrese el lado 3 de un triangulo: "))

if (l1 == l2 and l2 == l3):
    print("El triangulo es equilatero")
elif (l1 == l2 or l1 == l3 or l2 == l3):
    print("El triangulo es isoceles")
else:
    print("El triangulo es escaleno")

input()
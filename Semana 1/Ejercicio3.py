edad = int(input("Ingrese su edad: "))

if edad >= 18 and edad < 65:
    print("Bienvenido")
elif edad >= 65:
    print("Mostrar credencial del INSEN")
else:
    print("Vete :)")

input()

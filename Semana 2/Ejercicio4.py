horas = int(input("Ingrese las horas trabajadas: "))

if horas > 0 and horas <= 40:
    pago = horas * 16
elif horas > 40:
    extras = (horas - 40) * 20
    pago = (40 * 16) + extras
else:
    print("Numero invalido")

print("El pago por el bondadoso trabajo es $ ",pago)

input()
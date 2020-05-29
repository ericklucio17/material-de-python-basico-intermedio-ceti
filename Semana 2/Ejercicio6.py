cadena_resultado = "* |"
for contador in range (1, 10):
    cadena_resultado = cadena_resultado + str(contador).rjust(3," ")
cadena_resultado = cadena_resultado + "\n"

for contador in range (1, 32):
    cadena_resultado = cadena_resultado + "-"
cadena_resultado = cadena_resultado + "\n"

for fila in range (1, 10):
    cadena_resultado = cadena_resultado + str(fila) + " |"
    for columna in range (1, 10):
        multiplicacion = fila * columna
        cadena_resultado = cadena_resultado + str(multiplicacion).rjust(3, " ")
    cadena_resultado = cadena_resultado + "\n"

print(cadena_resultado)

input()
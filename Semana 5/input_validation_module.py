def input_int(mensaje):
    while True:
        try:
            entrada = int(input(mensaje))
        except ValueError:
            print("Información incorrecta, favor de capturar nuevamente")
            continue
        else:
            break
    return entrada

def input_float(mensaje):
    while True:
        try:
            entrada = float(input(mensaje))
        except ValueError:
            print("Información incorrecta, favor de capturar nuevamente")
            continue
        else:
            break
    return entrada
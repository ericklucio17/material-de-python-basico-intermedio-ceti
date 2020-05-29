from database_access import Inmueble
from datetime import datetime
from input_validation_module import input_float
from input_validation_module import input_int

fecha_actual = datetime.now().date()
while True:                
    print("---------- MENU ---------- \n" \
        + "1.- Registrar un inmueble \n" \
        + "2.- Actualizar un inmueble \n" \
        + "3.- Eliminar un inmueble \n" \
        + "4.- Consultar un inmueble por ID \n" \
        + "5.- Imprimir listado de inmuebles \n" \
        + "6.- Salir" \
        )
    opcion = input("Elige una opción:")

    if opcion=="1" :
        fecha_alta = fecha_actual
        id_tipo = input_int("Captura el tipo de inmueble (1-7):")
        id_operacion = input_int("Captura la operación del inmueble (1. Alquiler 2. Venta):")
        id_provincia = input_int("Captura la provincia (1-4):")
        superficie = input_float("Captura la superficie del inmueble:")
        precio_venta = input_float("Captura el precio de venta del inmueble:")
        fecha_venta = None
        id_vendedor = None
        inmueble = Inmueble(0, fecha_alta, id_tipo, id_operacion, id_provincia,superficie,
                        precio_venta, None, None)
        inmueble.agregar_inmueble()

    if opcion == "2":
        fecha_alta = fecha_actual
        id_inmueble = input_int("Captura el ID del inmueble a modificar:")
        id_tipo = input_int("Captura el tipo de inmueble (1-7):")
        id_operacion = input_int("Captura la operación del inmueble (1. Alquiler 2. Venta):")
        id_provincia = input_int("Captura la provincia (1-4):")
        superficie = input_float("Captura la superficie del inmueble:")
        precio_venta = input_float("Captura el precio de venta del inmueble:")
        fecha_venta = None
        id_vendedor = None
        inmueble = Inmueble(id_inmueble, fecha_alta, id_tipo, id_operacion, id_provincia,superficie,
                        precio_venta, None, None)
        inmueble.actualizar_inmueble()
    
    if opcion == "3":
        id_inmueble = input_int("Captura el ID del inmueble a eliminar:")
        inmueble = Inmueble(id_inmueble, None, 0,0,0,0,0,None, 0)
        inmueble.eliminar_inmueble()
        
    if opcion == "4":
        id_inmueble = input_int("Captura el ID del inmueble a consultar:")
        inmueble = Inmueble(id_inmueble, None, 0,0,0,0,0,None, 0)
        inmueble.consultar_inmueble_por_id()
 
    if opcion == "5":
        inmueble = Inmueble(0, None, 0,0,0,0,0,None, 0)
        inmueble.consultar_inmueble()
        

    if opcion == "6":
        break

    
input()
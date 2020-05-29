import mysql.connector
from mysql.connector import errorcode
from database_classes import Provincia

while (True):
    print("--- GESTION DE PROVINCIAS --- \n" \
    + "1.- Registrar una nueva provincia \n" \
    + "2.- Actualizar una provincia \n" \
    + "3.- Eliminar una provincia \n" \
    + "4.- Consultar una provincia por clave \n" \
    + "5.- Listar todas las provincias \n" \
    + "6.- Generar archivo de respaldo\n" \
    + "7.- Importar datos de un nuevo archivo\n" \
    + "8.- Salir \n" \
    )

    opcion = input("Eliga una opcion: ")

    if (opcion == "1"):
        idprovincia = int(input("Capture la clave de la provincia: "))
        provincia = input("Capture el nombre de la provincia: ")
        p = Provincia(idprovincia, provincia)
        p.registrar()

    if (opcion == "2"):
        idprovincia = int(input("Capture la clave de la provincia: "))
        provincia = input("Capture el nuevo nombre de la provincia: ")
        p = Provincia(idprovincia, provincia)
        p.actualizar()

    if (opcion == "3"):
        idprovincia = int(input("Capture la clave de la provincia: "))
        p = Provincia(idprovincia, '')
        p.eliminar()
    
    if (opcion == "4"):
        import mysql.connector
        from mysql.connector import errorcode
        
        idprovincia = input("Capture la clave de la provincia: ")
        p = Provincia(idprovincia, '')
        p.consultar()

    if (opcion == "5"):
        p = Provincia(0, '')
        p.listar()

    if (opcion == "6"):
        p = Provincia(0, '')
        p.generarArchivo()

    if (opcion == "7"):
        p = Provincia(0, '')
        p.importarArchivo()

    if (opcion == "8"):
        break
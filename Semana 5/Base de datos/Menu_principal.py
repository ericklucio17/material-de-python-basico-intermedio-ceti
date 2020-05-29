import mysql.connector
from mysql.connector import errorcode

while (True):
    print("--- GESTION DE PROVINCIAS --- \n" \
    + "1.- Registrar una nueva provincia \n" \
    + "2.- Actualizar una provincia \n" \
    + "3.- Eliminar una provincia \n" \
    + "4.- Consultar una provincia por clave \n" \
    + "5.- Listar todas las provincias \n" \
    + "6.- Salir \n" \
    )

    opcion = input("Eliga una opcion: ")

    if (opcion == "1"):
        idprovincia = int(input("Capture la clave de la provincia: "))
        provincia = input("Capture el nombre de la provincia: ")
        
        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "INSERT INTO provincia (id_provincia, nombre) VALUES (%(id_provincia)s, %(nombre)s)"
            
            datos_sentencia = {'nombre': provincia,
                        'id_provincia': idprovincia}
                        
            cursor.execute(sentencia, datos_sentencia)
            conn.commit()
            print("Registro agregado satisfactoriamente!")
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                conn.rollback()
        
        else:
            cursor.close()
            conn.close()

    if (opcion == "2"):
        idprovincia = int(input("Capture la clave de la provincia: "))
        provincia = input("Capture el nuevo nombre de la provincia: ")
        
        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "UPDATE provincia SET nombre = %(nombre)s WHERE id_provincia = %(id_provincia)s"
            
            datos_sentencia = {'nombre': provincia,
                            'id_provincia': idprovincia}
                            
            cursor.execute(sentencia, datos_sentencia)
            conn.commit()
            print("Registro actualizado satisfactoriamente!")
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                conn.rollback()
        else:
            cursor.close()
            conn.close()

    if (opcion == "3"):
        idprovincia = int(input("Capture la clave de la provincia: "))
        
        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "DELETE FROM provincia WHERE id_provincia = %(id_provincia)s"
            
            datos_sentencia = {'id_provincia': idprovincia}
            
            cursor.execute(sentencia, datos_sentencia)
            conn.commit()
            print("Registro eliminado satisfactoriamente!")
        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                conn.rollback()
        else:
            cursor.close()
            conn.close()
    
    if (opcion == "4"):
        import mysql.connector
        from mysql.connector import errorcode
        
        idprovincia = input("Capture la clave de la provincia: ")

        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "SELECT id_provincia, nombre FROM provincia WHERE id_provincia = %(id_provincia)s"

            datos_sentencia = {'id_provincia': idprovincia}
            cursor.execute(sentencia, datos_sentencia)
            Tabla = """\
                +---------------+
                | Clave   Nombre|
                |---------------|
                {}
                +---------------+\
                    """
            Tabla = (Tabla.format('\n'.join("| {} {}".format(*fila)    
                for fila in cursor)))

            print(Tabla)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)            
        else:
            cursor.close()
            conn.close()

    if (opcion == "5"):
        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "SELECT id_provincia, nombre FROM provincia"

            cursor.execute(sentencia)

            print("----------------------------------")
            for (id_provincia,  nombre) in cursor:
                cadena = "|{}|{}|".format(\
                str(id_provincia).rjust(5, " "),  nombre.ljust(26, " ")) + "\n"
                cadena = cadena + "----------------------------------"
                print(cadena)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)            
        else:
            cursor.close()
            conn.close()

    if (opcion == "6"):
        break
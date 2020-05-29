import mysql.connector
from mysql.connector import errorcode

class Provincia:
    def __init__(self, id_provincia, nombre):
        self.id_provincia = id_provincia
        self.nombre = nombre

    def registrar(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "INSERT INTO provincia (id_provincia, nombre) VALUES (%(id_provincia)s, %(nombre)s)"
            
            datos_sentencia = {'id_provincia': self.id_provincia, 'nombre': self.nombre}
                        
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

    def actualizar(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "UPDATE provincia SET nombre = %(nombre)s WHERE id_provincia = %(id_provincia)s"
            
            datos_sentencia = {'id_provincia': self.id_provincia, 'nombre': self.nombre}
                            
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

    def eliminar(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "DELETE FROM provincia WHERE id_provincia = %(id_provincia)s"
            
            datos_sentencia = {'id_provincia': self.id_provincia}
            
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

    def consultar(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()
            
            sentencia = "SELECT id_provincia, nombre FROM provincia WHERE id_provincia = %(id_provincia)s"

            datos_sentencia = {'id_provincia': self.id_provincia}
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
    
    def listar(self):
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

    #GUARDAR EN UN ARCHIVO DE EXCEL TODOS LOS CAMBIOS
    def generarArchivo(self):
        try:
            cadena_resultado = ""
            conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
            cursor = conn.cursor()

            sentencia = "SELECT id_provincia, nombre FROM provincia"

            datos_sentencia = {}
            cursor.execute(sentencia, datos_sentencia)
            fh = open("provincias_respaldo.csv", "w")
            for (id_provincia, nombre) in cursor:
                fh.write(str(id_provincia) + "," + nombre + "\n")
            fh.close()
            print("Archivo generado satisfactoriamente!")
        
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

    #IMPORTAR UN ARCHIVO DE EXCEL CON NUEVOS REGISTROS
    def importarArchivo(self):
        try:
            fh = open("nuevo_datos.csv")
            for line in fh.readlines():
                self.id_provincia = line.split(",")[0]
                self.nombre = line.split(",")[1]
                self.registrar()
            fh.close()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
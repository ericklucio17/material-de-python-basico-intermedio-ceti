import mysql.connector
from mysql.connector import errorcode

class Inmueble:

    def __init__(self, id_inmueble,  fecha_alta, id_tipo, id_operacion, id_provincia, superficie, precio_venta, fecha_venta, id_vendedor):
        self.id_inmueble = id_inmueble
        self.fecha_alta = fecha_alta
        self.id_tipo = id_tipo
        self.id_operacion = id_operacion
        self.id_provincia = id_provincia
        self.superficie = superficie
        self.precio_venta = precio_venta
        self.fecha_venta = fecha_venta
        self.id_vendedor = id_vendedor
    
    def consultar_inmueble(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456',
                                    host='127.0.0.1',
                                    database='inmobilaria')
            cursor = conn.cursor()

            sentencia = "SELECT id_inmueble,  fecha_alta, id_tipo, id_operacion, id_provincia, superficie, " \
                        + " precio_venta, fecha_venta, id_vendedor  FROM inmueble " \
                        #+ " WHERE id_inmueble = %(id_inmueble)s"

            #datos_sentencia = { 'id_inmueble': self.id_inmueble}
            datos_sentencia = {}
            cursor.execute(sentencia, datos_sentencia)
            for (id_inmueble,  fecha_alta, id_tipo, id_operacion, id_provincia, superficie, 
                precio_venta, fecha_venta, id_vendedor) in cursor:
                print("{},{},{},{},{},{},{},{},{}".format(\
                    id_inmueble,  fecha_alta, id_tipo, id_operacion, id_provincia, \
                    superficie, precio_venta, fecha_venta, id_vendedor))

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

    def consultar_inmueble_por_id(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456',
                                    host='127.0.0.1',
                                    database='inmobilaria')
            cursor = conn.cursor()

            sentencia = "SELECT id_inmueble,  fecha_alta, id_tipo, id_operacion, id_provincia, superficie, " \
                        + " precio_venta, fecha_venta, id_vendedor  FROM inmueble " \
                        + " WHERE id_inmueble = %(id_inmueble)s"

            datos_sentencia = {'id_inmueble': self.id_inmueble}
            cursor.execute(sentencia, datos_sentencia)
            for (id_inmueble,  fecha_alta, id_tipo, id_operacion, id_provincia, superficie, 
                precio_venta, fecha_venta, id_vendedor) in cursor:
                print("{},{},{},{},{},{},{},{},{}".format(\
                    id_inmueble,  fecha_alta, id_tipo, id_operacion, id_provincia, \
                    superficie, precio_venta, fecha_venta, id_vendedor))

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

    def agregar_inmueble(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456',
                                    host='127.0.0.1',
                                    database='inmobilaria')
            cursor = conn.cursor()

            sentencia = "INSERT INTO inmueble " \
                        + " (fecha_alta, id_tipo, id_operacion, id_provincia, superficie,  "\
                        + " precio_venta, id_vendedor) " \
                        + " VALUES (%(fecha_alta)s, %(id_tipo)s, %(id_operacion)s, %(id_provincia)s, "\
                        + " %(superficie)s, %(precio_venta)s, %(id_vendedor)s )"

            datos_sentencia = {'fecha_alta': self.fecha_alta, 
                                'id_tipo': self.id_tipo, 
                                'id_operacion': self.id_operacion, 
                                'id_provincia':self.id_provincia, 
                                'superficie':self.superficie,
                                'precio_venta':self.precio_venta ,
                                'id_vendedor':self.id_vendedor                                
                                }

            cursor.execute(sentencia, datos_sentencia)
            conn.commit()
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

    def actualizar_inmueble(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456',
                                    host='127.0.0.1',
                                    database='inmobilaria')
            cursor = conn.cursor()

            sentencia = "UPDATE inmueble SET " \
                        + " fecha_alta = %(fecha_alta)s, id_tipo = %(id_tipo)s, "\
                        + " id_operacion = %(id_operacion)s, id_provincia = %(id_provincia)s, "\
                        + " superficie = %(superficie)s, precio_venta = %(precio_venta)s, " \
                        + " id_vendedor = %(id_vendedor)s " \
                        + " WHERE id_inmueble = %(id_inmueble)s"

            datos_sentencia = { 'id_inmueble': self.id_inmueble,
                                'fecha_alta': self.fecha_alta, 
                                'id_tipo': self.id_tipo, 
                                'id_operacion': self.id_operacion, 
                                'id_provincia':self.id_provincia, 
                                'superficie':self.superficie,
                                'precio_venta':self.precio_venta ,
                                'id_vendedor':self.id_vendedor                                
                                }

            cursor.execute(sentencia, datos_sentencia)
            conn.commit()
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

    def vender_inmueble(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456',
                                    host='127.0.0.1',
                                    database='inmobilaria')
            cursor = conn.cursor()

            sentencia = "UPDATE inmueble SET " \
                        + " fecha_venta = %(fecha_venta)s, " \
                        + " id_vendedor = %(id_vendedor)s " \
                        + " WHERE id_inmueble = %(id_inmueble)s"

            datos_sentencia = { 'id_inmueble': self.id_inmueble,
                                'fecha_venta':self.fecha_venta ,
                                'id_vendedor':self.id_vendedor                                
                                }

            cursor.execute(sentencia, datos_sentencia)
            conn.commit()
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

    def eliminar_inmueble(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456',
                                    host='127.0.0.1',
                                    database='inmobilaria')
            cursor = conn.cursor()

            sentencia = "DELETE FROM inmueble " \
                        + " WHERE id_inmueble = %(id_inmueble)s"

            datos_sentencia = { 'id_inmueble': self.id_inmueble
                                }

            cursor.execute(sentencia, datos_sentencia)
            conn.commit()
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

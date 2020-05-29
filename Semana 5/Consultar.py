import mysql.connector
from mysql.connector import errorcode

idprovincia = int(input("Capture la clave de la provincia: "))

try:
    conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='inmobilaria')
    cursor = conn.cursor()
    
    sentencia = "SELECT * FROM provincia WHERE id_provincia = %(id_provincia)s"

            datos_sentencia = {'id_provincia': idprovincia}
            cursor.execute(sentencia, datos_sentencia)
            for (id_provincia) in cursor:
                print("{},{},{},{},{},{},{},{},{}".format(\
                    id_provincia)

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
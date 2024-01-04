

# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector


def connectionBD():
    print("ENTRO A LA CONEXION")
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host="monorail.proxy.rlwy.net",
                #host="monorail.proxy.rlwy.net:36320",
            port=36320,
            user="root",
            passwd="-eGGbb1B132D6gbHHB45CE451FA2DBe3",
                #passwd="-eGGbb1B132D6gbHHB45CE451FA2DBe3",
            database="railway",
                #database="crud_python",
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True

        )
        if connection.is_connected():
            print("Conexión exitosa a la BD")
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")

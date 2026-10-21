
import psycopg

try:
    with psycopg.connect(
        host="localhost",
        dbname="pvz_db",
        user="pvz_user",
        password="pvz123"
    ) as conexion:
        print("¡Conexión exitosa con PostgreSQL!")

except psycopg.OperationalError as error:
    print("No se pudo conectar:")
    print(error)

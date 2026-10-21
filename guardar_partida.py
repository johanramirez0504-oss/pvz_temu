
import psycopg

try:
    with psycopg.connect(
        host="localhost",
        dbname="pvz_db",
        user="pvz_user",
        password="pvz123"
    ) as conexion:

        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO partidas (
                    jugador_id,
                    puntuacion,
                    zombies_eliminados,
                    turnos
                )
                VALUES (%s, %s, %s, %s)
                """,
                (1, 250, 12, 30)
            )

        print("¡Partida guardada correctamente!")

except psycopg.Error as error:
    print("Error al guardar la partida:")
    print(error)

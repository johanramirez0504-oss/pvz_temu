
import psycopg

with psycopg.connect(
    host="localhost",
    dbname="pvz_db",
    user="pvz_user",
    password="pvz123"
) as conexion:

    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT
                jugadores.nombre,
                partidas.puntuacion,
                partidas.zombies_eliminados,
                partidas.turnos
            FROM partidas
            JOIN jugadores
                ON partidas.jugador_id = jugadores.id
            ORDER BY partidas.puntuacion DESC
        """)

        partidas = cursor.fetchall()

        for partida in partidas:
            nombre, puntuacion, zombies, turnos = partida

            print(
                f"Jugador: {nombre} | "
                f"Puntuación: {puntuacion} | "
                f"Zombis eliminados: {zombies} | "
                f"Turnos: {turnos}"
            )
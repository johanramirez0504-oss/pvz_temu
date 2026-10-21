
import psycopg
from getpass import getpass

def consultar_estadisticas():
    password = getpass("Contraseña de PostgreSQL: ")

    try:
        with psycopg.connect(
            host="localhost",
            dbname="pvz_db",
            user="pvz_user",
            password=password
        ) as conexion:

            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        j.id,
                        j.nombre,
                        COUNT(p.id) AS partidas,
                        COALESCE(SUM(p.puntuacion), 0) AS puntuacion_total,
                        COALESCE(SUM(p.zombies_eliminados), 0) AS zombies,
                        COALESCE(SUM(p.plantas_colocadas), 0) AS plantas,
                        COALESCE(SUM(p.soles_recolectados), 0) AS soles_recolectados,
                        COALESCE(SUM(p.soles_gastados), 0) AS soles_gastados,
                        COALESCE(SUM(p.turnos), 0) AS turnos,
                        COALESCE(SUM(p.oleadas_completadas), 0) AS oleadas
                    FROM jugadores j
                    LEFT JOIN partidas p ON p.jugador_id = j.id
                    GROUP BY j.id, j.nombre
                    ORDER BY puntuacion_total DESC;
                """)

                jugadores = cursor.fetchall()

                if not jugadores:
                    print("No hay jugadores registrados.")
                    return

                for jugador in jugadores:
                    (
                        id_jugador, nombre, partidas, puntuacion,
                        zombies, plantas, soles_rec, soles_gast,
                        turnos, oleadas
                    ) = jugador

                    print(f"\n{'=' * 35}")
                    print(f"Jugador: {nombre} (ID: {id_jugador})")
                    print(f"Partidas jugadas: {partidas}")
                    print(f"Puntuación total: {puntuacion}")
                    print(f"Zombis eliminados: {zombies}")
                    print(f"Plantas colocadas: {plantas}")
                    print(f"Soles recolectados: {soles_rec}")
                    print(f"Soles gastados: {soles_gast}")
                    print(f"Turnos acumulados: {turnos}")
                    print(f"Oleadas completadas: {oleadas}")

    except Exception as error:
        print("Error al consultar la base de datos:", error)


if __name__ == "__main__":
    consultar_estadisticas()


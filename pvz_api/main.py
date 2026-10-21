
from fastapi import FastAPI, HTTPException
import psycopg
import os
from getpass import getpass
from pydantic import BaseModel
app = FastAPI(title="Plantas vs. Zombies API")
class NuevaPartida(BaseModel):
    jugador_id: int
    puntuacion: int
    zombies_eliminados: int
    turnos: int
    plantas_colocadas: int
    soles_recolectados: int
    soles_gastados: int
    oleadas_completadas: int
    resultado: str


@app.post("/partidas")
def guardar_partida(partida: NuevaPartida):
    try:
        with conectar_db() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO partidas (
                        jugador_id, puntuacion,
                        zombies_eliminados, turnos,
                        plantas_colocadas, soles_recolectados,
                        soles_gastados, oleadas_completadas,
                        resultado
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    (
                        partida.jugador_id,
                        partida.puntuacion,
                        partida.zombies_eliminados,
                        partida.turnos,
                        partida.plantas_colocadas,
                        partida.soles_recolectados,
                        partida.soles_gastados,
                        partida.oleadas_completadas,
                        partida.resultado
                    )
                )
                nuevo_id = cursor.fetchone()[0]

        return {
            "mensaje": "Partida guardada correctamente",
            "partida_id": nuevo_id
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error guardando partida: {error}"
        )


def conectar_db():
    password = os.getenv("PVZ_DB_PASSWORD")

    if not password:
        password = getpass("Contraseña de PostgreSQL: ")

    return psycopg.connect(
        host="localhost",
        dbname="pvz_db",
        user="pvz_user",
        password=password
    )


@app.get("/")
def inicio():
    return {"mensaje": "API de Plantas vs. Zombies funcionando"}


@app.get("/jugadores")
def listar_jugadores():
    try:
        with conectar_db() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre FROM jugadores ORDER BY id"
                )
                filas = cursor.fetchall()

        return [
            {"id": fila[0], "nombre": fila[1]}
            for fila in filas
        ]

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error consultando jugadores: {error}"
        )
    
@app.get("/jugadores/{jugador_id}/partidas")
def listar_partidas(jugador_id: int):
    try:
        with conectar_db() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT jugadores.nombre, partidas.id, puntuacion, zombies_eliminados,
                           turnos, plantas_colocadas,
                           soles_recolectados, soles_gastados,
                           oleadas_completadas, resultado, fecha
                    FROM partidas
                    join jugadores on partidas.jugador_id = jugadores.id
                    WHERE jugador_id = %s
                    ORDER BY fecha DESC
                    """,
                    (jugador_id,)
                )
                filas = cursor.fetchall()

        return [
            {
                "jugador": fila[0],
                "id": fila[1],
                "puntuacion": fila[2],
                "zombies_eliminados": fila[3],
                "turnos": fila[4],
                "plantas_colocadas": fila[5],
                "soles_recolectados": fila[6],
                "soles_gastados": fila[7],
                "oleadas_completadas": fila[8],
                "resultado": fila[9],
                "fecha": fila[10]
            }
            for fila in filas
        ]

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error consultando partidas: {error}"
        )

    
@app.get("/jugadores/{jugador_id}/estadisticas")
def consultar_estadisticas(jugador_id: int):
    try:
        with conectar_db() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        j.nombre,
                        COUNT(p.id),
                        COALESCE(MAX(p.puntuacion), 0),
                        COALESCE(SUM(p.zombies_eliminados), 0),
                        COUNT(p.id) FILTER (
                            WHERE LOWER(p.resultado) = 'victoria'
                        ),
                        COUNT(p.id) FILTER (
                            WHERE LOWER(p.resultado) = 'derrota'
                        )
                    FROM jugadores j
                    LEFT JOIN partidas p ON p.jugador_id = j.id
                    WHERE j.id = %s
                    GROUP BY j.id, j.nombre
                    """,
                    (jugador_id,)
                )
                fila = cursor.fetchone()

        if fila is None:
            raise HTTPException(
                status_code=404,
                detail="Jugador no encontrado"
            )

        return {
            "jugador": fila[0],
            "partidas_jugadas": fila[1],
            "puntuacion_maxima": fila[2],
            "zombies_eliminados": fila[3],
            "victorias": fila[4],
            "derrotas": fila[5]
        }

    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error consultando estadísticas: {error}"
        )

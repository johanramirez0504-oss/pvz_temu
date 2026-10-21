# PvZ TEMU — Plants vs. Zombies in Python

A Plants vs. Zombies-inspired game developed in Python as a personal project to practice programming, game logic, resource management, and database integration.

## About the Project

**PvZ TEMU** is a project that combines a turn-based defense game with an API for managing and retrieving game data.

It uses Python for the game logic, FastAPI to provide a REST API, and PostgreSQL to store player and game information.

## Features

- **Plant System:** Place plants with different costs, health values, and abilities.
- **Zombies and Waves:** Defend the garden against advancing zombies.
- **Resource Management:** Collect and spend sun to place plants.
- **Combat System:** Use plant abilities and zombie attributes during gameplay.
- **Sound Effects:** Includes audio files to enhance the gaming experience.
- **REST API:** Register completed games and retrieve player information.
- **Database Integration:** Store game results and player statistics using PostgreSQL.
  <img width="1154" height="1161" alt="image" src="https://github.com/user-attachments/assets/e51e2257-4a1d-4967-9970-7050cdc1958d" />


## Technologies

| Technology | Purpose |

| Python | Core game logic |
| FastAPI | REST API development |
| PostgreSQL | Relational database |
| Psycopg | PostgreSQL connectivity |
| Pydantic | Data validation |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
pvz_temu/
├── pvzTEMU.py
├── sonidos/
├── pvz_api/
│   └── main.py
├── guardar_partida.py
├── consultar_partidas.py
├── consultar_estadisticas.py
├── probar_db.py
└── README.md
```

*The structure may vary depending on the auxiliary files included in the repository.*

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/johanramirez0504-oss/pvz_temu.git
cd pvz_temu
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```powershell
.venv\Scripts\activate
```

### 3. Install the dependencies

For the API, install:

```bash
pip install fastapi "uvicorn[standard]" "psycopg[binary]" pydantic
```

Install any additional libraries required by the game, including audio-related dependencies used in the source code.

### 4. Run the game

From the project root directory:

```bash
python3 pvzTEMU.py
```

### 5. Configure and run the API

Make sure PostgreSQL is installed and running. Create a database named `pvz_db`, configure the required database user, and create the tables expected by the application.

Set the database password as an environment variable:

```bash
export PVZ_DB_PASSWORD="your_password"
```

Start the API:

```bash
cd pvz_api
python -m uvicorn main:app --reload
```

The API will be available locally at:

- **API root:** http://127.0.0.1:8000/
- **Interactive API documentation:** http://127.0.0.1:8000/docs

> Never commit real passwords, credentials, or other secrets to the repository.

## API Endpoints

| Method | Endpoint | Description |

| `GET` | `/` | Check whether the API is running |
| `GET` | `/jugadores` | Retrieve registered players |
| `POST` | `/partidas` | Register a game |
| `GET` | `/jugadores/{jugador_id}/partidas` | Retrieve a player's game history |
| `GET` | `/jugadores/{jugador_id}/estadisticas` | Retrieve a player's statistics |

You can test the endpoints and inspect request formats through `/docs` while the API server is running.

## Project Goals

This project provides hands-on experience with:

- Designing functions and working with data structures.
- Implementing game mechanics and resource management.
- Building a REST API with FastAPI.
- Connecting Python applications to a relational database.
- Storing and retrieving game data.
- Using Git and GitHub for version control.

## Author

**Johan Ramirez**

A personal learning project focused on applying programming concepts to a playable game and a backend API.

---

*PvZ TEMU — Combining game development, Python, and backend engineering.*

import random
import pygame 
import psycopg
from getpass import getpass
import requests
pygame.mixer.init()
sonido_ataque=pygame.mixer.Sound("sonidos/ataque2.mp3")
sonido_explosion=pygame.mixer.Sound("sonidos/explosion.mp3")
musica_fondo=pygame.mixer.music.load("sonidos/musica.mp3")
poner_planta=pygame.mixer.Sound("sonidos/poner_planta.mp3")
grito_perdedor=pygame.mixer.Sound("sonidos/grito_perdedor.mp3")
perdiste=pygame.mixer.Sound("sonidos/perdiste.mp3")
risa_demonio=pygame.mixer.Sound("sonidos/risa_demonio.mp3")
zombie_come=pygame.mixer.Sound("sonidos/zombie_come.mp3")
felicidades=pygame.mixer.Sound("sonidos/felicidades.mp3")
ganar=pygame.mixer.Sound("sonidos/ganar.mp3")
you_lose=pygame.mixer.Sound("sonidos/you_lose.mp3")
pala=pygame.mixer.Sound("sonidos/pala.mp3")
start=pygame.mixer.Sound("sonidos/start.mp3")
touch=pygame.mixer.Sound("sonidos/touch.mp3")
plantas= {
            1:{
                "nombre":"🌻",
                "costo": 50,
                "vida": 5
                },
            2:{
                "nombre":"🫛",
                "costo": 100,
                "vida": 10,
                "ataque": 5            
                },
            3:{
                "nombre":"🌰",
                "costo": 75,
                "vida": 50
                },
            4:{
                "nombre":"🍒",
                "costo": 250,
                "vida": 1,
                "ataque": 500

                }
            }
zombies={
            1:{
                "zombie":"🧟",
                "vida": 9,
                "ataque": 5
                },
            2:{
                "zombie":"🧌",
                "vida": 18,
                "ataque": 10
                },
            3:{
                "zombie":"👹",
                "vida": 4,
                "ataque": 3000
                }
            }
modelos_zombies=("🧟","🧌","👹")
modelos_plantas=("🌻","🫛","🌰","🍒")
def pvz(plantas,zombies,jugador_id):
    salir=True

    while salir:
        print("="*20)
        print("=PlantasVsZombies=".center(20,"="))
        print("🧟‍".center(19,"="))
        print("🌱"*10)
        print("PERO DE TEMU\n")
        jardin = [
            ["🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱"],
            ["🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱"],
            ["🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱"],
            ["🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱"],
            ["🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱", "🌱"]
        ]
        estadisticas = {
    "zombies_eliminados": 0,
    "plantas_colocadas": 0,
    "soles_recolectados": 0,
    "soles_gastados": 0,
    "turnos": 0,
    "oleadas_completadas": 0
}       

        zombies[1]["vida"] = 9
        zombies[1]["ataque"] = 5
        zombies[2]["vida"] = 18
        zombies[2]["ataque"] = 10
        vida_zom={}
        vida_plantas={}
        soles=1500
        back=True
        oleada=3
        cantidad_zombies=random.randint(10,20)
        conteo=0
        while back:
                print(vida_plantas)
                print(f"Cantidad de zombies: {cantidad_zombies}")
                print(f"Oleada: {oleada}")
                ataque_planta(jardin,zombies,plantas,vida_zom,estadisticas,modelos_zombies,vida_plantas,soles,modelos_plantas)
                derrota=mover_zombies(jardin,vida_zom,vida_plantas,zombies,plantas,soles,modelos_plantas,modelos_zombies)
                if derrota:
                    pygame.mixer.music.stop()
                    perdiste.play()
                    grito_perdedor.play()
                    print("PERDISTE\nLos Zombies se comieron tu cerebro 🧟🧠🧟")
                    print("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠖⢋⣡⡴⢗⠯⢛⠒⢌⣵⢖⣪⣥⣏⣒⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢄⡖⠋⠄⢂⠘⠊⡁⠄⢂⠐⠠⡸⠋⠠⢉⢐⡔⢒⣏⡝⡜⣍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣵⡟⣱⠈⡐⠠⢈⠐⠀⠂⠄⡈⠐⠠⢁⠂⠄⠂⠄⠩⢸⢿⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⢿⣿⣿⣡⢏⠠⠐⡀⠂⠠⠁⡈⠄⠠⠁⠂⠄⡈⠄⠡⠈⠄⠟⣜⢃⡌⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⡚⣦⠀⠡⢀⠁⢂⠐⠀⠄⠁⠄⠡⠐⢠⠈⠡⢈⡐⣢⢯⢸⢠⢠⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⣿⢡⡏⡷⣌⡐⠠⢈⠀⡐⠈⠠⠈⠄⠡⠈⠄⣈⣐⡶⢎⣸⣯⠺⠘⣿⡞⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀1⢸⣿⣿⢆⣿⢗⣣⣝⣣⣏⡽⠽⣦⠁⠐⡈⠄⡁⢲⠞⢍⣒⣉⣳⡇⡇⢹⣿⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢛⡿⣿⣟⡾⢸⣿⣿⣷⣫⢶⣩⣽⠄⢡⣰⣆⣐⣠⣾⡷⡶⣬⣸⣜⡅⣻⢹⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣵⠛⣿⢭⢻⣿⣿⣿⣽⣷⡷⣣⢌⣿⣿⢊⠹⣪⣸⢿⡧⣔⢯⡟⡇⣯⣻⣿⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣎⣯⠽⡪⣝⢿⣿⣿⣿⠿⣊⡌⣾⣿⣿⣧⢒⠻⢤⣃⣳⣣⣇⢸⠀⣿⡝⡼⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⣿⣧⣓⣮⣭⣯⡽⢦⡹⣼⣼⣿⣿⣿⣿⡎⡵⣪⢗⣩⠟⡔⣝⣴⣿⢽⢱⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣚⣷⣿⣿⡟⡭⢚⡾⣱⣎⣛⣟⣹⣭⣿⣻⣷⡡⣟⢻⣛⡞⢹⣿⣷⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⣟⣸⣟⣽⣿⣽⣻⣽⣫⢷⣿⠈⣿⣿⣮⢬⡹⠇⣼⣿⢟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⢿⡹⢆⡿⣾⣿⣿⠀⣸⣆⣧⣸⣿⣼⣿⣿⣿⣖⡟⠀⣿⣷⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣿⡙⢾⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⠀⡏⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡞⣏⠖⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣀⣀⡀⠀⠀⠀⠀⠀⢀⡀⢹⡜⢮⡹⣿⣿⣿⡹⣿⣿⣿⣿⣿⣿⣿⣿⢯⣼⡞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢰⢏⡻⣹⠹⣿⠳⣌⢳⢣⡛⣷⠀⣀⣴⢤⡌⢹⠀⣟⣦⢓⡝⣿⢻⣷⣻⡏⣿⠁⣿⢻⣼⣟⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢀⡴⣒⢶⡟⢦⠳⣥⢫⡟⡳⣌⢧⢣⡝⣼⣾⢻⡌⡿⠱⠈⠀⡗⡾⣷⡔⣹⣿⡶⢯⣟⣿⢻⣻⣭⣾⣻⡿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠸⣜⡱⣾⣙⣎⠳⢦⢳⣏⡵⢪⡜⣱⢚⡼⣏⠶⣩⡇⢠⣷⣾⣷⡵⣿⣿⡱⢎⡿⣿⣾⣷⢿⡳⣛⣭⣿⢧⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣷⢣⢽⣗⡧⡈⠉⣏⢾⣗⣪⠷⣼⣡⣿⢺⢧⡛⡴⢳⣾⣿⣿⣿⣿⣽⣿⣏⣳⣜⡼⡍⣎⢧⣓⣋⣼⡿⣾⣿⣿⣗⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢻⡗⡺⣿⢐⡃⠀⡯⣿⡿⠀⠀⠀⠀⡿⣿⡟⢮⣱⣽⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣿⡿⢿⢟⡛⣟⢫⣽⣿⣿⣿⣿⣿⣷⣾⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢸⣧⠱⠘⣷⡦⣖⠳⢭⡗⡰⡆⢀⣿⡟⠼⣃⣿⢱⣏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⠦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⢸⣣⣕⡸⠱⣍⠿⣷⣯⡽⣩⢏⡼⡅⢛⣸⠆⣻⣬⣷⣾⣿⣿⣿⣿⣿⣿⠛⢿⡿⠟⠛⣻⢿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣽⣶⣒⣒⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠁⠀⠀⠀⠹⣞⣹⢿⣻⣟⣿⣽⢿⣯⣷⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⠟⠀⣸⡬⠶⠼⡄⠸⡆⢀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠙⠚⠩⠭⢿⡞⣿⣻⣟⣿⣟⣿⣾⣿⣿⣿⣿⣿⠙⢦⣀⡾⠋⢀⣀⣤⣀⣄⠈⢀⡀⠀⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡽⣳⢄⡙⠻⣇⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⢯⣁⣟⠛⠋⠫⠻⢿⣿⣿⡿⠃⢠⠀⣸⣽⡾⠉⠄⠂⠀⠉⠻⡦⠤⡆⠹⠐⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⢗⣣⢛⣼⢢⣌⡙⠶⢄⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠀⠀⠀⠹⠷⣀⣀⣘⣔⡠⣀⣀⣐⡨⠞⠋⠉⠓⢦⠀⠐⠓⠞⣶⡗⣋⠀⡄⠳⡄⠴⡾⠿⠿⣿⣿⣿⣿⣿⣷⣬⠳⣌⠳⣎⡝⣯⡸⡆⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠎⠿⣷⣶⣤⡄⠠⠀⢠⣾⣀⠄⠠⣴⠟⠁⠀⢰⣠⣤⠤⣦⠀⠀⠀⢀⡿⠄⠀⣷⡀⢻⡄⠁⠒⠂⠈⢿⣿⣿⣿⣿⣡⢛⡬⢳⡜⡜⢦⢧⡇⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠀⡀⠀⠙⠚⣤⡀⠘⢿⣻⡃⠀⡁⣅⣊⠜⢀⢸⡏⠐⠤⠊⠀⢀⣢⣾⣁⣤⡾⠃⠘⢻⡤⠀⣆⢠⣠⣾⣿⣿⣿⣿⣖⢫⡜⣣⠞⡹⣼⣼⠁⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣏⣷⠶⠲⠦⣤⡴⠀⠈⢹⡄⣀⠙⢷⡆⠀⠀⠀⠠⢀⣾⢧⡈⠶⠶⠶⠿⣛⠿⠛⠉⠀⡤⢁⢤⠇⣭⣧⡈⠁⠛⠿⣿⣿⣿⣿⡜⡼⣡⢏⣽⣿⠃⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣴⠏⠀⢐⢈⣄⠁⠀⠄⠁⣾⠿⠉⠁⡀⢻⣬⡴⠓⠛⣿⠏⢉⠈⢉⠢⠤⠤⠐⠀⡀⠀⣴⠧⡊⠂⣰⠟⠙⣷⣈⣀⣀⣸⣿⣿⠷⣙⠶⡱⢎⢶⣽⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢰⡇⡀⢨⣼⠋⠀⠠⣈⣴⢾⡏⠐⠊⢧⣤⣼⠿⠧⣀⡀⠛⠈⠁⠠⠘⠦⣦⣤⡥⠶⢾⡛⠁⠀⣐⣤⠅⠀⢢⠯⣍⢏⣷⢻⡛⣭⢚⡥⣳⢳⣛⡿⢿⣫⢭⢦⠀⠀⠀
        ⠀⠀⠀⠀⠀⣾⡀⠀⢸⡇⠀⠠⠘⠉⠈⠹⢧⡀⠈⣼⠏⢁⠔⠀⣐⣈⣤⣦⣅⣀⠠⠀⠀⡄⡄⠩⠂⠹⣿⠟⠉⠀⢤⡼⠿⢽⡘⣾⢥⣛⠷⣌⢳⣾⣧⠳⣌⣧⣈⣷⡍⡿⡆⠀⠀
        ⠀⠀⠀⠀⠀⠘⢷⣠⠀⠉⠠⣰⠇⠀⣠⠀⠈⠁⠀⣿⡀⠄⡀⠐⠋⠁⠀⢀⠈⠙⠍⣊⠑⠸⡎⠀⡐⢠⡟⡀⣸⢌⠾⠱⠁⣸⣱⣿⣎⣜⡳⣌⣿⠿⢽⣿⢔⡚⣞⢹⣆⡳⢧⡀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠊⠛⢶⣤⣼⣦⣌⣤⡾⠿⣧⡀⠐⠀⠂⢀⣤⣞⣀⣐⣀⣀⣀⣼⠃⣁⡰⣋⣠⣴⣿⢚⡮⢦⣴⡿⣿⣿⠉⠀⠘⣶⡇⠀⠀⠹⣞⣸⠊⠸⣿⣟⠁⠙⣄
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠙⠛⠲⠞⠻⠿⠶⠟⠋⠉⠛⠛⠛⠿⠿⠿⠟⠛⠋⠉⠛⠛⠋⠉⠀⠻⡏⢤⡇⣸⠝⠁⠀⠀⠀⣿⣾⠀⡇⢿⡿⠷⣴⠼
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠛⠛⢣⣲⣀⠇⠀⠀⠀
        """)
                    you_lose.play()
                    guardar_partida(estadisticas, "Derrota",jugador_id, calcular_puntuacion(estadisticas))
                    estadisticas_juego(estadisticas,puntuacion=calcular_puntuacion(estadisticas))                                                   

                    back=volver_juego_salir(back)
                    if not back:
                        continue
                    else:
                        return
                
                zombie,conteo=colocar_zombies(jardin,vida_zom,zombies,oleada,cantidad_zombies,conteo)
                if zombie==0:
                    continue
                mostrar(jardin,soles)
                soles,salir=jugador_turno(plantas,soles,jardin,vida_plantas,estadisticas,salir,vida_zom)
                if salir==False:
                    break
                estadisticas["turnos"]+=1
                
                if len(vida_zom)==0 and conteo>=cantidad_zombies:
                    oleada+=1
                    cantidad_zombies=random.randint(3,5)
                   
                    zombies[1]["vida"]+=oleada*10
                    zombies[1]["ataque"]+=oleada*5
                    zombies[2]["vida"]+=oleada*10
                    zombies[2]["ataque"]+=oleada*5                    
                    conteo=0
                    estadisticas["oleadas_completadas"]+=1
                    if oleada>3:
                        pygame.mixer.music.stop()
                        ganar.play()
                        felicidades.play()
                        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⡴⠗⠦⡀⣀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡤⣄⣾⠀⠈⢻⡁⠀⠀⢹⠁⢹⠁⠀⢹⣠⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣸⡀⠠⡙⢧⠴⠚⠉⠉⠉⠉⠉⠉⠑⠲⢼⡁⡀⢀⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡁⠀⢈⠙⣦⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢾⡉⠀⣹⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⠖⠒⠳⣄⣈⠟⠁⠀⠀⠀⡴⣶⡀⠀⠀⠀⠀⠀⣶⣆⠀⠀⠙⣟⡭⠉⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢧⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠈⢦⠶⠧⣄
⢈⡷⠶⠤⣼⠀⠀⠀⠀⠀⠀⠻⠿⠃⠀⠀⠀⠀⠀⠛⠋⠀⣀⠀⠀⣸⠀⣀⡼
⣏⠀⠀⠒⠺⡄⠀⠒⠻⢦⣤⣀⣀⣀⠀⠀⠀⠀⢀⣀⣠⡴⠟⠁⢠⠟⠛⠳⣅⠀⠀
⠈⠓⢒⡶⠚⣳⣄⠀⠀⠀⠀⠉⠻⢿⣛⣿⣛⡿⠋⠉⠁⠀⢀⡴⠣⢤⡤⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣞⠀⠈⠁⣨⠗⠤⣀⠀⠀⠀⠀⠈⠉⠁⠀⠀⣀⣠⠴⠯⣄⡀⠀⡳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⠒⠒⢻⠁⠀⣰⠃⢹⠓⡶⠒⠒⢶⠒⠒⣯⠑⠘⢧⣀⣹⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠓⠚⠹⣄⠀⣠⣇⠀⠀⡼⡦⠴⣋⣧⣤⣞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠁⠈⠓⡺⡇⢳⡎⠁⠀⡸⠟⠒⠐⠒⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡸⠦⠤⠤⢌⣺⡌⢿⢠⡾⠊⠁⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡊⠁⠀⠀⠀⠐⠒⠚⠛⠚⣏⠀⠀⠀⠀⢀⡠⢤⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣸⠀⡀⠀⡠⠋⠀⣀⡷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⣠⠒⠉⠐⠢⢄⣀⣀⣠⠶⠃⠑⠷⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        """,end=" ")
                        print("""
⣿⢿⣻⢿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⡿⣿
⣿⣻⢯⣿⣻⢾⡽⣷⢯⣷⢿⣽⢾⣻⣾⡽⣷⢯⣷⢿⣽⢾⣻⣾⣽⣷⠿⠿⢛⠻⣷⣿⣿⠛⢻⣿⡿⢛⣾⣯⣷⣿⣷⣯⢿⡾⣽⡾⣯⡷⣟⣷⣯⢿⡾⣽⡾⣯⡷⣟⣷⣯⢿⣽⢿
⣿⡽⣟⣷⢿⣻⢿⣽⣻⡽⣿⢾⣻⣽⣞⣿⣽⣻⡽⣿⡾⠿⣿⣾⣻⣧⣸⡀⢸⣶⣿⣿⣿⠀⣾⣿⡇⢸⣿⣿⠏⢠⣿⣿⢯⣟⣯⡿⣷⣟⣯⣷⣻⣯⣟⣯⢿⡷⣟⣯⣷⣻⣟⣾⢿
⣿⡽⣿⢾⣻⣯⢿⡽⣯⣿⣽⣻⢯⣷⢿⣾⣷⣟⣿⣻⣧⢢⠘⢿⣿⡿⣿⡇⠘⣿⣿⣻⡿⠀⣿⣿⡇⣿⣿⡟⠀⣾⣿⣯⢿⣯⣷⣿⠷⣿⣟⣾⢷⣻⣾⣻⢯⣟⡿⣽⣞⡿⣞⣯⣿
⣿⣽⢯⣿⣳⢿⣯⢿⣷⣻⣞⡿⣯⣿⡟⢉⠙⢿⣿⡿⣿⠘⢓⡀⠹⣿⣿⣿⠀⢻⣿⣿⣿⡀⠛⠛⣠⣿⣿⠁⣸⣿⣿⣽⣟⣾⠟⣫⠀⣼⣿⣯⢿⣻⡾⣽⣟⣯⣿⣻⢾⣟⡿⣽⣾
⣿⢾⣻⣷⣻⣟⣾⣟⣾⡽⣯⣟⣿⣇⠀⢻⠇⠸⢿⣿⣿⡈⢿⣿⣄⣬⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣌⣉⣸⡿⠟⣡⣈⠃⢰⣿⣿⣻⡟⠻⣿⣿⣾⡽⣞⣯⣿⢾⣻⣟⣾
⣿⣻⢷⣯⡷⣟⣷⢯⣿⣽⠟⢿⣿⣿⣷⣄⠘⢶⣄⠈⣻⣷⣾⣿⣿⣿⠿⣿⣽⠾⠟⠛⠉⠉⠉⠉⠻⢿⣽⣻⢿⣿⣿⣷⣾⣿⠏⢀⣿⣿⣟⣿⠗⠃⡌⠻⣿⣽⢿⣽⡾⣿⣽⢾⣻
⣿⣿⣿⣾⣿⣿⣾⣿⣿⠃⣶⣾⡿⢻⣿⣿⣦⢀⣿⣿⣿⣿⣿⠟⠃⠀⢰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⡿⢿⣿⣿⣿⣷⣼⣿⣿⡿⢃⣤⣾⣧⣾⣿⣿⣿⣾⣿⣷⣿⣿⣿
⣿⣻⣿⣻⣽⡿⣽⢿⣿⡀⢿⣿⣿⣄⠈⢻⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⡀⠤⠤⢀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠉⠻⣿⣿⡿⣿⡍⢠⣿⣿⣿⣿⣿⠟⠙⢿⣿⣟⡿⣯⣟⣿
⣿⣳⣯⣷⢯⣿⣯⣿⢿⣷⣄⠉⠛⠛⢁⣼⣿⣿⡿⠋⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀⠙⢦⠀⠀⠀⣠⠞⠁⠀⠀⠈⠑⢄⠀⠈⠻⣿⣿⣿⣿⣿⡿⠟⠋⣠⣴⣾⣿⡿⣞⣿⣽⣻⢾
⣿⣳⢿⣞⣿⣧⣉⡛⠿⢿⣿⣿⣷⣾⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⡎⠀⠀⠀⢀⣀⡀⠀⠀⢇⠀⡰⠁⠀⢀⠀⢀⠀⠀⠈⢆⠀⠀⠙⣷⣿⢾⣷⣄⣴⣿⣿⠿⠿⠻⠿⣿⣷⣯⣟⣿
⣿⡽⣯⣿⡾⠟⠛⠋⠉⢀⣀⣉⣽⣿⣯⣷⡏⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢰⣱⡃⣈⣆⠀⢸⠀⡇⠀⠀⣧⣇⣠⢡⠀⠀⢸⠀⠀⠀⠘⣿⣟⡿⣿⣿⠏⢁⣤⣶⣿⣶⠈⣿⣷⡿⣾
⣿⣽⢯⣿⣷⣦⣬⣙⡛⠿⠿⣿⣿⣿⣳⡿⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠸⣻⣿⡿⡘⠀⡸⠀⡇⠀⢀⡽⣿⡿⡹⠇⠀⠰⠀⠀⠀⠀⢸⣿⣟⣷⣿⡀⠻⣿⠿⠟⠃⣠⣿⣿⡽⣿
⣿⢾⣻⣷⣻⣿⣿⣿⣿⣷⣦⣿⣿⢷⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠱⢄⣀⠈⠣⠒⠊⠀⣠⠃⠀⠘⣄⠀⠉⠐⠂⢁⠠⠤⠃⠀⠀⠀⠀⠀⣿⣿⣞⣿⣿⣶⣤⣴⣶⣿⣿⣿⣯⢿⣽
⣿⣻⣽⠟⢁⣠⣤⣄⡉⠻⣿⣿⣽⣻⣯⡅⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠈⠐⠠⡠⠖⠁⠀⠀⠀⠈⠢⡤⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢾⣳⣿⡟⠿⠿⠟⠛⠛⠛⢻⣿⣿
⣿⡽⣿⡀⠻⣿⣿⣿⡿⠂⣿⣿⡷⣿⣽⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⡢⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⡏⠀⠀⠀⠀⠀⣿⣿⣻⣟⣾⣷⣾⣿⠟⠋⣀⣴⣿⣿⣯
⣿⡽⣿⣿⣦⣤⣀⣀⣤⣴⣿⣿⣽⣻⣽⣧⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣦⣄⡈⠉⠒⠒⠂⠀⠀⠐⠒⠒⠊⠉⣠⣿⡿⠁⠀⠀⠀⠀⢸⣿⣟⣷⣯⢿⣟⣉⣀⣐⣈⣉⣉⣙⣿⣿
⣿⡽⣷⣿⣿⣿⣿⣿⠟⠻⣿⣷⣯⢿⣽⡿⠦⢄⡡⠀⡀⠂⠄⢠⢿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣤⣤⣤⣤⣶⣶⣿⣿⡿⠁⠀⠀⠀⠀⣠⡿⠿⢿⣾⡽⣿⣿⠿⢿⣿⣿⣿⣿⣿⡿⣽
⣿⣽⣿⠁⣴⣿⣷⣿⣿⠆⢹⣿⣯⢿⡇⠀⠀⠀⠉⢆⠄⡡⢈⠄⠫⣿⣿⣿⣿⣿⣿⡿⣿⣻⡿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⡶⠁⠀⠀⠀⣾⣟⣿⠇⣰⣿⡟⠉⣉⠙⢿⣿⣽
⣿⣞⣿⣷⣈⡙⠛⠉⣁⣠⣿⣿⢯⣿⡇⠀⠀⠀⠀⢸⡇⢆⠡⢂⠄⡐⠝⡿⣿⣭⣭⣙⣳⢿⣭⣉⣙⣻⡿⠟⠁⠀⠀⠀⠀⠠⣾⠃⠀⠀⠀⠀⣿⡿⣿⣦⣈⣉⣀⣴⡿⠃⣼⣿⣻
⣿⢾⣽⣻⣿⢿⣿⣿⣿⡿⣟⣯⣿⢾⠇⠀⠀⠀⠀⠘⠛⠚⠓⠣⠎⣄⠀⠈⠀⠉⠓⠛⠋⠟⠙⠛⠋⠁⠀⠀⠀⣀⡤⠖⠚⠛⠛⠃⠀⠀⠀⠀⢸⣿⣻⢿⡿⣿⣿⣿⣿⣿⣿⣟⣿
⣿⢯⣷⣟⣾⢿⣽⢾⣳⣿⣻⣽⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢆⠄⣀⢀⠒⠤⠠⢄⢂⡀⢀⠠⣀⣶⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢯⣟⣷⣟⣾⣳⢿⡾⣽⣾
⣿⢯⣷⣻⡽⣟⣾⣟⡿⣾⣽⣳⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣶⣮⣴⣌⣸⣀⣏⣴⣦⣼⣾⣷⣿⡿⠃⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠈⣿⣯⢿⡾⣽⣾⣻⢯⣟⡿⣾
⣿⣯⣿⣽⣻⣯⣷⣿⣽⣷⣯⣟⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣻⣟⣿⣿⣿⣿⣻⣿⣽⣯⣟⣾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣯⣟⣿⣽⣞⣯⣿⣯⣿⣽
⣿⢿⣿⣿⣿⢿⣿⡿⣿⣿⡿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⢿⣿⣿⣿⣿⡿⣿⣿⢿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⣿⣿⡿⣿⣿⣿⢿⣿⣿
⣿⣻⣽⢾⣻⣟⡷⣿⣻⣽⣻⣽⡾⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣯⢿⣻⡾⣽⣾⣻⢯⣟⡿⣽⣳⡿⣿⡆⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡽⣿⣽⣻⢯⣟⣾⢯⣿⢾
⣿⣽⢾⣟⡿⣞⡿⣷⣻⢷⣻⡷⣟⣿⡿⣷⣤⣄⣀⣀⣀⣀⣀⣤⣾⣿⣻⢾⡿⣽⣻⣽⣾⣻⢯⣟⣿⡽⣯⢿⣽⢿⣦⣤⣀⣀⣀⣀⣀⣠⣴⣾⣿⣟⡷⣿⣳⣯⣟⡿⣽⣯⢿⡾⣿
⣿⢾⣻⣽⣻⢿⣽⣻⣽⣟⣯⢿⣯⣯⣟⢭⣻⡿⣿⢿⡿⣿⢿⣟⡿⣾⣽⣻⣽⢿⣽⣳⣯⣟⡿⣽⣾⣻⣽⢿⡽⣯⡿⣽⢿⡿⣿⣿⡿⣷⡷⣽⣻⡾⣟⣷⣟⣷⣻⢿⣽⡾⣿⣽⣻
⣿⣻⣽⢷⣻⣯⣿⣷⣿⣾⣯⢿⣻⣾⣼⡽⣟⣝⢿⣯⣿⡽⣟⣾⣟⣷⢯⣟⣾⣯⡷⣟⣷⣻⣽⣟⣾⡽⣯⣟⣿⣽⣻⢯⣿⢫⣽⡽⡵⣳⣿⡿⣿⣽⣻⢷⣻⡾⣯⣿⢾⣽⡷⣯⢿
⣿⣽⢾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣽⣞⣿⣻⣿⣮⣻⣲⣻⣹⡿⣣⢿⡞⣿⣯⣷⢯⣟⡿⣽⣻⣾⣽⣾⣻⣽⣿⢾⢷⢿⣿⣻⢭⣿⣼⣾⣿⣻⣽⢷⣯⣟⡿⣽⣻⢷⣯⡿⣾⣽⣟⣿
⣿⢾⣻⣽⣿⣿⣿⣿⣾⣿⣿⢿⣽⡾⣷⣻⣾⣽⣻⢿⣷⡟⣱⣿⣻⣻⣾⣍⣏⢻⢹⣿⢽⡇⣿⣽⠻⣟⡼⣵⣷⣏⣯⣷⡿⣿⣻⣽⢷⣯⡷⣟⣿⢾⣽⣻⢯⣟⡿⣾⣽⢷⣻⣾⣽
⣿⣻⣽⢷⣻⡿⣿⣿⣿⢿⣯⡿⣾⣽⢷⣟⡷⣯⣟⡿⣞⣿⢿⣽⣻⣟⡿⣿⣿⣒⣼⣿⣽⣷⣿⣿⣾⡿⣿⢿⣻⣟⣯⣷⢿⣯⣟⣾⣟⣾⣽⢿⣾⣻⣽⢯⡿⣯⢿⣳⣯⣿⣻⢾⣽
⣿⣽⢾⣟⣯⢿⣳⣟⣾⢯⣷⣟⡿⣞⣯⡿⣽⣟⣾⣟⣯⣟⡿⣞⣷⢿⣽⣷⣻⣟⡿⣽⣾⣳⣟⣾⣳⢿⣯⣟⡿⣾⣽⢾⣟⣾⣽⣳⣯⣟⣾⣟⣾⣽⡾⣟⣿⡽⣟⣯⣷⢯⣟⣯⣿
""")
                        print("¡Enhorabuena! Has superado este Plantas vz Zombies de Temu.")
                        guardar_partida(estadisticas, "Victoria",jugador_id, calcular_puntuacion(estadisticas))
                        estadisticas_juego(estadisticas,puntuacion=calcular_puntuacion(estadisticas))
                        back=volver_juego_salir(back)
                        if not back:
                            continue
                        else:
                            return
                    print(f"\n\nTHE ZOMBIES ARE COMING 🧟:Oleada {oleada}\n\n")
                    
#TURNO DEL JUEGO                    
def jugador_turno(plantas,soles,jardin,vida_plantas,estadisticas,salir,vida_zom):
        turno=True
        
        while turno:
            try:
                
                planta=colocar_planta(jardin,plantas,estadisticas,vida_plantas,modelos_plantas)
                if planta==5:
                    mostrar(jardin,soles)
                    continue
                if planta==6:
                    soles,turno=opciones(jardin,soles,turno,estadisticas)
                    continue
                if planta==7:
                    salir=False
                    return soles,salir
                if planta==0:
                    continue
                numero_planta=planta
                planta=plantas[planta]
                costo=planta["costo"]
                
                if soles<costo:
                    print(f"Tienes {soles}☀️ y esta planta cuesta {costo}☀️, no tienes suficientes soles.")
                    continue
                print(f"Has elegido {planta['nombre']} con un costo de {planta['costo']}☀️. Te quedan {soles-costo}☀️")
                fila_jardin=int(input("Introduzca la fila para colocar la planta: "))-1
                touch.play()
                columna_jardin=int(input("Introduzca la columna para colocar la planta: "))-1
                touch.play()
                if not fila_jardin in range(5) or not columna_jardin in range(9) :
                    print("❌ Coordenada inválida. Elige una posición entre 1-5 y 1-9.")
                    continue
                if jardin[fila_jardin][columna_jardin]=="🌱":
                    poner_planta.play()
                    jardin[fila_jardin][columna_jardin]=planta["nombre"]
                    vida_plantas[(fila_jardin, columna_jardin)] = planta["vida"]
                    soles-=costo
                    estadisticas["soles_gastados"]+=costo
                    estadisticas["plantas_colocadas"]+=1
                    if numero_planta==4:
                        petacereza(jardin,fila_jardin,columna_jardin,vida_zom,plantas,soles,estadisticas,modelos_zombies)
                        del vida_plantas[(fila_jardin, columna_jardin)]
                        break
                    else:
                        soles, turno = opciones(jardin, soles, turno,estadisticas)

                else:
                    print("Ya esta casilla está ocupada, elige otra.")
                    continue
            except ValueError:
                print("Opción no disponible.")
        return soles,salir
#Opciones para salir o volver
def opciones(jardin,soles,turno,estadisticas):
    while turno:
        terminar_turno=input("Desea terminar turno? S/N: ").upper().strip()
        start.play()
        if terminar_turno=="S":
            soles=producir_soles(jardin,soles,estadisticas)
            turno=False
            return soles,turno
        elif terminar_turno=="N":
            mostrar(jardin,soles)
            turno=True
            return soles,turno
            
        else:
            print("Solo S o N.")
def volver_juego_salir(back):
    while back:
        volver_juego=input("\nDeseas volver a jugar? S/N: ").upper().strip()
        start.play()
        if volver_juego=="S":
            pygame.mixer.music.play(-1)
            return False   
        elif volver_juego=="N":
            pygame.mixer.music.play(-1)
            print("Cerrando juego...")
            return True
        else:
            print("Solo S o N sesudo.")
            
#Jardin: Muestra el jardin actualizado
def mostrar(jardin,soles):
    print(f"Tienes {soles}☀️\n️")
    print("   1  2  3  4  5  6  7  8  9")

    for numero, fila in enumerate(jardin, 1):
        print(numero, " ".join(fila))
        
#Plantas: Para colocar, atacar, defender o producir soles    
def colocar_planta(jardin,plantas,estadisticas,vida_plantas,modelos_plantas):
        planta=int(input("\n¿Qué planta quieres? Elige el número: 1.🌻 2.🫛. 3.🌰 4.🍒 5.🪏️ 6.Skip ⏭️ 7.Volver al menú ↩️\n"))
        start.play()
        if planta==5:
            print("Excavando...")
            remover_planta(jardin,vida_plantas,modelos_plantas)
            return 5
        if planta==6:
            print("Saltando turno...")
            return 6
        if planta==7:
            return 7
        elif planta not in plantas:
            print("Opción no disponible.")
            return 0
        return planta
    
def producir_soles(jardin,soles,estadisticas):
    for filas in jardin:
            for casilla in filas:
                if casilla=="🌻":
                    soles+=25
                    estadisticas["soles_recolectados"]+=25
    return soles

def ataque_planta(jardin,zombies,plantas,vida_zom,estadisticas,modelos_zombies,vida_plantas,soles,modelos_plantas):
    for fila in range(len(jardin)):
        for columna in range(len(jardin[fila]) - 1, -1, -1):
            if jardin[fila][columna]=="🫛":
                for posicion in range(columna+1,len(jardin[fila])):
                    if jardin[fila][posicion] in modelos_zombies:
                        print("El lanzaguisantes se ha encontrado un zombie.")
                        sonido_ataque.play()
                        vida_zom[(fila, posicion)] -= plantas[2]["ataque"]
                        if jardin[fila][posicion]=="👹":
                            if vida_zom[(fila, posicion)]<=0:
                                del vida_zom[(fila, posicion)]
                                estadisticas["zombies_eliminados"]+=1
                                jardin[fila][posicion]="🌱"
                                print("demonio ha muerto.")
                                evil_demon_zombie(jardin,fila,posicion,vida_zom,vida_plantas,estadisticas,modelos_zombies,zombies,modelos_plantas,soles)

                        elif vida_zom[(fila, posicion)]<=0:
                            
                            del vida_zom[(fila, posicion)]
                            estadisticas["zombies_eliminados"]+=1
                            jardin[fila][posicion]="🌱"
                            print("Zombie ha muerto.")

                        break
def petacereza(jardin,fila_jardin,columna_jardin,vida_zom,plantas,soles,estadisticas,modelos_zombies):
    casillas_explosion=[]
    for i in range(fila_jardin-1, fila_jardin+2):
        for j in range(columna_jardin-1, columna_jardin+2):
            if i in range(5) and j in range(9) and (i,j)!=(fila_jardin,columna_jardin):
                if jardin[i][j] in modelos_zombies:
                    print("La petacereza se encontró con un zombie")
                    vida_zom[(i, j)] -= plantas[4]["ataque"]

                    if vida_zom[(i, j)] <= 0:
                        del vida_zom[(i, j)]
                        jardin[i][j] = "🌱"
                        estadisticas["zombies_eliminados"] += 1

                casillas_explosion.append((i, j, jardin[i][j]))

    for i, j, contenido in casillas_explosion:
        jardin[i][j] = "🔥"
        
    jardin[fila_jardin][columna_jardin] = "💥"
    mostrar(jardin, soles)
    sonido_explosion.play()
    for i, j, contenido in casillas_explosion:
        jardin[i][j] = contenido
    jardin[fila_jardin][columna_jardin] = "🌱"

#Zombies: Aparecen, atacan  y avanzan
def colocar_zombies(jardin,vida_zom,zombies,oleada,cantidad_zombies,conteo):
    columna=8
    fila=random.randint(0,4)
    if cantidad_zombies<=conteo:
        return 1,conteo
    if oleada>=3:
        for x in range(0,5):
            
            if jardin[x][columna]=="🌱":
                colocar=random.randint(0,10)           
                if colocar in (6,5):
                    
                    
                    jardin[x][columna]="🧌"
                    vida_zom[(x,columna)]=zombies[2]["vida"]
                    conteo+=1
                elif colocar==4:
                    jardin[x][columna]="👹"
                    risa_demonio.play()
                    vida_zom[(x,columna)]=zombies[3]["vida"]
                    conteo+=1
                elif colocar in (1,2,3):
                    
                    jardin[x][columna]="🧟"
                    vida_zom[(x,columna)]=zombies[1]["vida"] 
                    print("Ha aparecido un zombie")
                    conteo+=1

                
                        
        return 1,conteo
    elif oleada==2:
        if jardin[fila][columna]=="🌱":
            colocar=random.randint(0,3)           
            if colocar==3:
                jardin[fila][columna]="🧌"
                vida_zom[(fila,columna)]=zombies[2]["vida"]
            else:
                jardin[fila][columna]="🧟"
                vida_zom[(fila,columna)]=zombies[1]["vida"]
            print("Ha aparecido un zombie")
            conteo+=1
            return 1,conteo
    else:
        if jardin[fila][columna]=="🌱":
            colocar=random.randint(0,3)           
            jardin[fila][columna]="🧟"
            vida_zom[(fila,columna)]=zombies[1]["vida"]
            print("Ha aparecido un zombie")
            conteo+=1
            return 1,conteo
    return 0,conteo

def mover_zombies(jardin,vida_zom,vida_plantas,zombies,plantas,soles,modelos_plantas,modelos_zombies):
    for fila in range(len(jardin)):
        for columna in range(len(jardin[fila])):
            if jardin[fila][columna] in modelos_zombies:
                if columna==0:
                    return True
                if jardin[fila][columna] == "👹":

                    if columna >= 2:

                        plantas_incineradas = []
                        zombies_incinerados = []
                        hay_planta = False

                        for posicion in (columna - 1, columna - 2):
                            if jardin[fila][posicion] in modelos_plantas:
                                hay_planta = True
                        if hay_planta:
                            for posicion in (columna - 1, columna - 2):

                                if jardin[fila][posicion] in modelos_plantas:
                                    plantas_incineradas.append(posicion)
                                    del vida_plantas[(fila, posicion)]

                                elif jardin[fila][posicion] in modelos_zombies:
                                    zombies_incinerados.append(posicion)
                                    del vida_zom[(fila, posicion)]
                                jardin[fila][columna-1] = "🔥"
                                jardin[fila][columna-2] = "🔥"

                            mostrar(jardin, soles)

                            for posicion in zombies_incinerados:
                                jardin[fila][posicion] = "💀️"

                                mostrar(jardin, soles)

                            jardin[fila][columna-1] = "🌱"
                            jardin[fila][columna-2] = "🌱"

                            
                                
                if jardin[fila][columna-1] in modelos_zombies:
                    pass
                elif jardin[fila][columna-1] in modelos_plantas:
                    
                    print("El zombie se ha encontrado con una planta")
                    if jardin[fila][columna]=="🧟":
                        vida_plantas[(fila,columna-1)]-=zombies[1]["ataque"]
                        zombie_come.play()
                    elif jardin[fila][columna]=="🧌":
                        vida_plantas[(fila,columna-1)]-=zombies[2]["ataque"]
                        zombie_come.play()
                    elif jardin[fila][columna]=="👹":
                        vida_plantas[(fila,columna-1)]-=zombies[3]["ataque"]
                        zombie_come.play()

                    if vida_plantas[(fila,columna-1)]<=0:
                        print("Una planta ha sido comida por un zombie")
                        jardin[fila][columna-1]="🌱"
                        del vida_plantas[(fila,columna-1)]
                        
                else:
                    if jardin[fila][columna]=="🧟":
                        vida=vida_zom[(fila,columna)]
                        jardin[fila][columna]="🌱"
                        jardin[fila][columna-1]="🧟"
                        del vida_zom[(fila,columna)]
                        vida_zom[(fila, columna-1)] = vida
                    elif jardin[fila][columna]=="🧌":
                        vida=vida_zom[(fila,columna)]
                        jardin[fila][columna]="🌱"
                        jardin[fila][columna-1]="🧌"
                        del vida_zom[(fila,columna)]
                        vida_zom[(fila, columna-1)] = vida
                    elif jardin[fila][columna]=="👹":
                        vida=vida_zom[(fila,columna)]
                        jardin[fila][columna]="🌱"
                        jardin[fila][columna-1]="👹"
                        del vida_zom[(fila,columna)]
                        vida_zom[(fila, columna-1)] = vida
    return False
def evil_demon_zombie(jardin,fila,posicion,vida_zom,vida_plantas,estadisticas,modelos_zombies,zombies,modelos_plantas,soles):
    casillas_explosion=[]
    for i in range(fila-1, fila+2):
        for j in range(posicion-1, posicion+2):
            if i in range(5) and j in range(9) and (i,j)!=(fila,posicion):
                if jardin[i][j] in modelos_zombies:
                    vida_zom[(i, j)] -= zombies[3]["ataque"]
                    if vida_zom[(i, j)] <= 0:
                        del vida_zom[(i, j)]
                        jardin[i][j] = "🌱"
                        estadisticas["zombies_eliminados"] += 1
                elif jardin[i][j] in modelos_plantas:
                    vida_plantas[(i, j)] -= zombies[3]["ataque"]
                    if vida_plantas[(i, j)]<=0:
                        del vida_plantas[(i, j)]
                        jardin[i][j] = "🌱"

                casillas_explosion.append((i, j, jardin[i][j]))

    for i, j, contenido in casillas_explosion:
        jardin[i][j] = "🔥"
        
    jardin[fila][posicion] = "💥"
    mostrar(jardin, soles)
    sonido_explosion.play()
    for i, j, contenido in casillas_explosion:
        jardin[i][j] = contenido
    jardin[fila][posicion] = "🌱"

    
    
#Pala: Para remover una planta de una casilla
def remover_planta(jardin,vida_plantas,modelos_plantas):
        pala_fila=int(input("Fila de la planta a eliminar: "))-1
        touch.play()
        pala_columna=int(input("Columna de la planta a eliminar: "))-1
        touch.play()
        if pala_fila not in range(5) or pala_columna not in range(9):
            print("\nEsta casilla no está en el tablero\n")
        elif jardin[pala_fila][pala_columna] in modelos_plantas:
            del vida_plantas[(pala_fila,pala_columna)]
            jardin[pala_fila][pala_columna]="🌱"
            pala.play()
        else:
            print("Aquí no hay una planta")
            
#Para mostrar las estadisticas almacenadas de la partida           
def estadisticas_juego(estadisticas, puntuacion):
    stats=input("¿Deseas ver tus estadísticas? S/N:").upper().strip()
    start.play()
    if stats=="S":
        print("\nESTADÍSTICAS\n".center(38,"="))
        print(f'\nTurnos: {estadisticas["turnos"]}')
        print(f'Plantas: {estadisticas["plantas_colocadas"]}')
        print(f'Muertos: {estadisticas["zombies_eliminados"]}')
        print(f'Oleadas superadas: {estadisticas["oleadas_completadas"]}')
        print(f'Soles recolectados: {estadisticas["soles_recolectados"]}')
        print(f'Soles gastados: {estadisticas["soles_gastados"]}')
        print(f'Puntuación: {puntuacion}')
    else:
        pass

def explicacion_rapida():
    print("""
🎯 OBJETIVO
Sobrevive a todas las oleadas y evita que los
zombies lleguen al extremo izquierdo.

☀️ SOLES
Utiliza los soles para comprar plantas.
Las 🌻 producen soles al terminar tu turno.

🌱 PLANTAS
Cada planta tiene diferentes características,
como costo y vida.

🧟 ZOMBIES
Aparecen por el lado derecho y avanzan hacia
la izquierda.

⚔️ COMBATE
Las plantas atacan automáticamente a los zombies
que estén en su misma fila.

🪏️ PALA
Utilízala para eliminar una planta.

🏆 VICTORIA
Elimina todas las oleadas.

💀 DERROTA
Si un zombie llega al extremo izquierdo, pierdes.
""")

    input("\nPresiona ENTER para volver...")
    start.play()
def explicacion_detallada():
    print("""
📚 EXPLICACIÓN DETALLADA

🎯 OBJETIVO
Tu objetivo es defender el jardín de las oleadas
de zombies. Los zombies aparecen por el lado
derecho y avanzan hacia la izquierda.

☀️ SISTEMA DE SOLES
Los soles son el recurso utilizado para colocar
plantas. Algunas plantas tienen un costo mayor
que otras.

Las 🌻 producen soles al finalizar el turno.
La cantidad producida depende de las 🌻 que
tengas colocadas.

🌱 COLOCAR PLANTAS
Para colocar una planta debes seleccionar una
posición válida del jardín y tener suficientes
soles para pagar su costo.

Cada planta tiene una cantidad de vida diferente.

⚔️ ATAQUES DE LAS PLANTAS
Las plantas que pueden atacar buscan zombies
en su misma fila.

Cuando una planta ataca, reduce la vida del
zombie. Si su vida llega a 0, el zombie es
eliminado.

🧟 MOVIMIENTO DE LOS ZOMBIES
Los zombies avanzan una posición hacia la
izquierda cuando pueden.

Si encuentran una planta directamente delante
de ellos, la atacan en lugar de avanzar.

Si un zombie llega al extremo izquierdo del
jardín, la partida termina.

🪏️ PALA
La pala permite eliminar una planta que ya
esté colocada en el jardín.

🔄 TURNOS
Durante tu turno puedes colocar plantas,
utilizar la pala o saltar el turno.

Al terminar el turno, las 🌻 producen soles.

🌊 OLEADAS
Cuando todos los zombies de una oleada son
eliminados, comienza una nueva.

Las oleadas posteriores son más difíciles.

🏆 VICTORIA
Completa todas las oleadas para ganar la partida.

💀 DERROTA
Pierdes si un zombie consigue llegar al extremo
izquierdo del jardín.
""")

    input("\nPresiona ENTER para volver...")
    start.play()

def instrucciones_juego():
    while True:
        print("\n" + "="*30)
        print("        📖 CÓMO JUGAR")
        print("="*30)

        print("""
1. ⚡ Explicación rápida
2. 📚 Explicación detallada
3. ↩️ Volver
""")
        op_info = input("Selecciona una opción: ")
        if op_info == "1":
            start.play()
            explicacion_rapida()

        elif op_info == "2":
            start.play()
            explicacion_detallada()

        elif op_info == "3":
            start.play()
            break

        else:
            print("Opción inválida.")

def mostrar_plantas(plantas):
    while True:
        print("\n" + "="*30)
        print("          🌱 PLANTAS")
        print("="*30)

        print("""
1. ⚡ Información rápida
2. 📚 Información detallada
3. ↩️ Volver
""")

        op_plant = input("Selecciona una opción: ")

        if op_plant == "1":
            start.play()
            plantas_rapido(plantas)

        elif op_plant == "2":
            start.play()
            plantas_detallado(plantas)

        elif op_plant == "3":
            start.play()
            break

        else:
            print("Opción inválida.")

def plantas_rapido(plantas):
    print(f"""
🌱 PLANTAS DISPONIBLES

1. 🌻 Girasol
   ☀️ Produce 25 soles
   💰 Costo: {plantas[1]['costo']}
   ❤️ Vida: {plantas[1]['vida']}

2. 🫛 Lanzaguisantes
   ⚔️ Ataca zombies
   💰 Costo: {plantas[2]['costo']}
   ❤️ Vida: {plantas[2]['vida']}
   💥 Ataque: {plantas[2]['ataque']}

3. 🌰 Nuez
   🛡️ Tiene mucha vida
   💰 Costo: {plantas[3]['costo']}
   ❤️ Vida: {plantas[3]['vida']}

4. 🍒 Petacereza
   💥 Explota y daña zombies cercanos
   💰 Costo: {plantas[4]['costo']}
   ❤️ Vida: {plantas[4]['vida']}
   💥 Ataque: {plantas[4]['ataque']}
""")

    input("\nPresiona ENTER para volver...")
def plantas_detallado(plantas):
    print(f"""
📚 INFORMACIÓN DETALLADA DE LAS PLANTAS

🌻 GIRASOL
El girasol es una planta que no ataca a los zombies.
Su función principal es producir soles.

💰 Costo: {plantas[1]['costo']} soles
❤️ Vida: {plantas[1]['vida']}

Al finalizar tu turno, cada girasol colocado
produce soles.

────────────────────────────

🫛 LANZAGUISANTES
El lanzaguisantes es una planta ofensiva.
Ataca automáticamente a los zombies que se
encuentren en su misma fila.

💰 Costo: {plantas[2]['costo']} soles
❤️ Vida: {plantas[2]['vida']}
💥 Ataque: {plantas[2]['ataque']}

Es especialmente útil para eliminar zombies
antes de que avancen demasiado.

────────────────────────────

🌰 NUEZ
La nuez es una planta defensiva.

💰 Costo: {plantas[3]['costo']} soles
❤️ Vida: {plantas[3]['vida']}

Tiene mucha más vida que las demás plantas,
por lo que puede resistir varios ataques
de los zombies.

Su función principal es servir como defensa
y retrasar el avance de los zombies.

────────────────────────────

🍒 PETACEREZA
La petacereza es una planta explosiva.
Al colocarla, explota inmediatamente y daña
a los zombies que se encuentren cerca de ella.

💰 Costo: {plantas[4]['costo']} soles
❤️ Vida: {plantas[4]['vida']}
💥 Ataque: {plantas[4]['ataque']}

Su explosión afecta las casillas cercanas,
por lo que puede eliminar varios zombies
al mismo tiempo.
""")

    input("\nPresiona ENTER para volver...")
def zombies_rapido(zombies):
    print(f"""
🧟 ZOMBIES DISPONIBLES

1. 🧟 Zombie normal
   ❤️ Vida: {zombies[1]['vida']}
   ⚔️ Ataque: {zombies[1]['ataque']}

2. 🧌 Zombie fuerte
   ❤️ Vida: {zombies[2]['vida']}
   ⚔️ Ataque: {zombies[2]['ataque']}

3. 👹 Zombie demonio
   ❤️ Vida: {zombies[3]['vida']}
   ⚔️ Ataque: {zombies[3]['ataque']}
""")

    input("\nPresiona ENTER para volver...")
    start.play()

def zombies_detallado(zombies):
    print(f"""
📚 INFORMACIÓN DETALLADA DE LOS ZOMBIES

🧟 ZOMBIE NORMAL

Es el zombie básico del juego.
Avanza hacia la izquierda del jardín y ataca
a las plantas que encuentre en su camino.

❤️ Vida: {zombies[1]['vida']}
⚔️ Ataque: {zombies[1]['ataque']}

Es el zombie más común y puede aparecer
durante las diferentes oleadas.

────────────────────────────

🧌 ZOMBIE FUERTE

Es una versión más resistente y poderosa
que el zombie normal.

❤️ Vida: {zombies[2]['vida']}
⚔️ Ataque: {zombies[2]['ataque']}

Tiene más vida y causa más daño a las plantas,
por lo que puede ser más difícil de eliminar.

────────────────────────────

👹 ZOMBIE DEMONIO

Es el zombie más peligroso del juego.
Además de avanzar y atacar, puede realizar
un ataque especial que afecta varias casillas
cercanas.

❤️ Vida: {zombies[3]['vida']}
⚔️ Ataque: {zombies[3]['ataque']}

Su ataque especial puede destruir plantas
y otros zombies que se encuentren cerca.

Aparece con mayor frecuencia en las oleadas
más avanzadas.
""")

    input("\nPresiona ENTER para volver...")
    start.play()

def mostrar_zombies(zombies):
    while True:
        print("\n" + "="*30)
        print("          🧟 ZOMBIES")
        print("="*30)

        print("""
1. ⚡ Información rápida
2. 📚 Información detallada
3. ↩️ Volver
""")

        op_zombie = input("Selecciona una opción: ")

        if op_zombie == "1":
            start.play()
            zombies_rapido(zombies)

        elif op_zombie == "2":
            start.play()
            zombies_detallado(zombies)

        elif op_zombie == "3":
            start.play()
            break

        else:
            print("Opción inválida.")
def calcular_puntuacion(estadisticas):
    zombis = estadisticas["zombies_eliminados"]
    oleadas = estadisticas["oleadas_completadas"]

    puntuacion = (zombis * 10) + (oleadas * 50)

    return puntuacion

def guardar_partida(estadisticas, resultado, jugador_id, puntuacion):
    datos = {
        "jugador_id": jugador_id,
        "puntuacion": puntuacion,
        "zombies_eliminados": estadisticas["zombies_eliminados"],
        "turnos": estadisticas["turnos"],
        "plantas_colocadas": estadisticas["plantas_colocadas"],
        "soles_recolectados": estadisticas["soles_recolectados"],
        "soles_gastados": estadisticas["soles_gastados"],
        "oleadas_completadas": estadisticas["oleadas_completadas"],
        "resultado": resultado.lower()
    }

    try:
        respuesta = requests.post(
            "http://127.0.0.1:8000/partidas",
            json=datos,
            timeout=10
        )

        respuesta.raise_for_status()

        print("Partida guardada correctamente mediante la API.")

    except requests.RequestException as error:
        print("No se pudo guardar la partida mediante la API:", error)


db_password = None


def obtener_jugador_id():
    global db_password

    if db_password is None:
        db_password = getpass("Contraseña de PostgreSQL: ")

    nombre = input("Introduce tu nombre de jugador: ").strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return None

    try:
        with psycopg.connect(
            host="localhost",
            dbname="pvz_db",
            user="pvz_user",
            password=db_password
        ) as conexion:

            with conexion.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM jugadores WHERE nombre = %s",
                    (nombre,)
                )

                jugador = cursor.fetchone()

                if jugador is not None:
                    return jugador[0]

                cursor.execute(
                    """
                    INSERT INTO jugadores (nombre)
                    VALUES (%s)
                    RETURNING id
                    """,
                    (nombre,)
                )

                return cursor.fetchone()[0]

    except Exception as error:
        print("No se pudo identificar al jugador:", error)
        return None
def main_menu(plantas,zombies,jugador_id):
        pygame.mixer.music.play(-1)
        while True:
            print("""
OPCIONES DEL MENÚ:\n
\t1-Jugar 🎮\n\t2-Intrucciones de cómo jugar 📖\n\t3-Información de plantas 🌻\n\t4-Información de zombies 🧟\n\t5-Salir 🚪
""")
            op=input("Elige una opciones: ")
            if op=="1":
                start.play()
                jugador_id = obtener_jugador_id()
                pvz(plantas,zombies,jugador_id) 
            elif op=="2":
                start.play()
                instrucciones_juego()
            elif op=="3":
                start.play()
                mostrar_plantas(plantas)
            elif op=="4":
                start.play()
                mostrar_zombies(zombies)
            elif op=="5":
                start.play()
                print("Saliendo del programa...")
                return
            else:
                print("Opción no válida")
                
main_menu(plantas,zombies,jugador_id=None)

def barrer_trapear():
    print("Sistema para saber si te toca barrer o trapear.")
    conteo_barrer=0
    conteo_trapear=0
    for _ in range(5):
        input("Presiona enter: ")
        valor=random.randint(0,1)
        if valor==0:
            print("Punto para barrer")
            conteo_barrer+=1
        elif valor==1:
            print("Punto para trapear")
            conteo_trapear+=1
        if conteo_barrer==3:
            print("Felicidades, te toca barrer.")
            break
        elif conteo_trapear==3:
            print("Felicidades, te toca trapear.")
            break
    pass
def m():
    can_num_int=int(input("Cuántos numeros enteros contendrá la lista?: "))
    lista=[]
    for _ in range(can_num_int):
        lista.append(int(input("Introduce un número entero: ")))
    print(f"{lista}")
    print(f"La sumatoria de todos los elementos de la lista es de: {sum(lista)}")
    pass
def x():
    lista=["A","B","b","c","E","E","f"]
    print(f"Lista original: {lista}")
    remove_ele=input("Introduce el elemento que deseas eliminar: ")
    for _ in lista:
        if remove_ele.lower() in lista:
            lista.remove(remove_ele.lower())
        elif remove_ele.upper() in lista:
            lista.remove(remove_ele.upper())
    print(f"Nueva lista: {lista}")
    pass
def w():
    lista=[1,2,3,4,5]
    lista_eliminados=[]
    print(f"Lista números: {lista}.")
    lista_eliminados.append(lista.pop(0))
    lista_eliminados.append(lista.pop(-1))

    print(f"Lista números: {lista}.")
    print(f"Lista eliminados: {lista_eliminados}.")
    pass
def g():
    batallas = [
        ["Johan", 120, [30, 25, 40, 15]],
        ["Carlos", 200, [50, 45, 60]],
        ["Luis", 150, [20, 30, 25, 40]],
        ["Ana", 90, [40, 35, 50]],
        ["Maria", 180, [35, 40, 30, 45]]
    ]
    conteo=0
    daño_acumulado=0
    primero=True
    daño_mayor=0
    daño_menor=0
    mejor_jugador=""
    peor_jugador=""
    mejor_ataque=0
    mejor_jugador_ataque=""
    for personaje in batallas:
        conteo+=1
        jugador=personaje[0]
        vida=personaje[1]
        ataques=personaje[2]
        daño_total=0
        ataque_mayor=0
        for daño in ataques:
            daño_total+=daño
            if daño>ataque_mayor:
                ataque_mayor=daño
            if daño>mejor_ataque:
                mejor_ataque=daño
                mejor_jugador_ataque=jugador
        daño_acumulado+=daño_total
        print(f"Jugador: {jugador}, Daño total: {daño_total}, su mayor ataque es de: {ataque_mayor}.")
        if primero:
            peor_jugador=jugador
            daño_menor = daño_total
            primero = False
        if daño_total>daño_mayor:
            daño_mayor=daño_total
            mejor_jugador=jugador
        if daño_total<daño_menor:
            daño_menor=daño_total
            peor_jugador=jugador
    daño_promedio=daño_acumulado/conteo
    print(f"\nEl mayor daño fue de: {daño_mayor}, provocado por {mejor_jugador}.")
    print(f"El menor daño fue de: {daño_menor}, provocado por {peor_jugador}.")
    print(f"El daño promedio fue de: {daño_promedio}, con un daño acumulado de {daño_acumulado}.")
    print(f"El el ataque con mayor daño fue de: {mejor_ataque}, provocado por {mejor_jugador_ataque}.")
    pass

import random
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
def pvz(plantas,zombies):
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
        vida_zom={}
        vida_plantas={}
        soles=2500
        back=True
        oleada=3
        cantidad_zombies=random.randint(8,20)
        conteo=0
        while back:
                print(vida_plantas)
                print(f"Cantidad de zombies: {cantidad_zombies}")
                print(f"Oleada: {oleada}")
                ataque_planta(jardin,zombies,plantas,vida_zom,estadisticas,modelos_zombies,vida_plantas,soles,modelos_plantas)
                derrota=mover_zombies(jardin,vida_zom,vida_plantas,zombies,plantas,soles,modelos_plantas,modelos_zombies)
                if derrota:
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
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢛⡿⣿⣟⡾⢸⣿⣿⣷⣫⢶⣩⣽⠄⢡⣰⣆⣐⣠⣾⡷⡶⣬⣸⣜⡅⣻⢹⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
        ⢻⡗⡺⣿⢐⡃⠀⡯⣿⡿⠀⠀⠀⡿⣿⡟⢮⣱⣽⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣿⡿⢿⢟⡛⣟⢫⣽⣿⣿⣿⣿⣿⣷⣾⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
                    estadisticas_juego(estadisticas)                                                   

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
                
                if len(vida_zom)==0 and conteo==cantidad_zombies:
                    cantidad_zombies=random.randint(oleada*3+10,oleada*5+15)
                    oleada+=1
                    zombies[1]["vida"]+=oleada*10
                    zombies[1]["ataque"]+=oleada*5
                    zombies[2]["vida"]+=oleada*10
                    zombies[2]["ataque"]+=oleada*5                    
                    conteo=0
                    estadisticas["oleadas_completadas"]+=1
                    if oleada>3:
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
                        
                        estadisticas_juego(estadisticas)
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
                    print(f"Tienes {soles}☀️ y esta planta cuesta {costo}, no tienes suficientes soles.")
                    continue
                print(f"Has elegido {planta['nombre']} con un costo de {planta['costo']}. Te quedan {soles-costo}☀️")
                fila_jardin=int(input("Introduzca la fila para colocar la planta: "))-1
                columna_jardin=int(input("Introduzca la columna para colocar la planta: "))-1
                if not fila_jardin in range(5) or not columna_jardin in range(9) :
                    print("❌ Coordenada inválida. Elige una posición entre 1-5 y 1-9.")
                    continue
                if jardin[fila_jardin][columna_jardin]=="🌱":
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
        if volver_juego=="S":
            return False   
        elif volver_juego=="N":
            print("Cerrando juego...")
            return True
        else:
            print("Solo S o N sesudo.")
            
#Jardin: Muestra el jardin actualizado
def mostrar(jardin,soles):
    print(f"Tienes {soles}☀\n️")
    print("   1  2  3  4  5  6  7  8  9")

    for numero, fila in enumerate(jardin, 1):
        print(numero, " ".join(fila))
        
#Plantas: Para colocar, atacar, defender o producir soles    
def colocar_planta(jardin,plantas,estadisticas,vida_plantas,modelos_plantas):
        planta=int(input("\n¿Qué planta quieres? Elige el número: 1.🌻 2.🫛. 3.🌰 4.🍒 5.🪏️ 6.Skip ⏭️ 7.Volver al menú ↩️\n"))
        if planta==5:
            print("Excavando...")
            remover_planta(jardin,vida_plantas,modelos_plantas,modelos_plantas)
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
    for i, j, contenido in casillas_explosion:
        jardin[i][j] = contenido
    jardin[fila_jardin][columna_jardin] = "🌱"

#Zombies: Aparecen, atacan  y avanzan
def colocar_zombies(jardin,vida_zom,zombies,oleada,cantidad_zombies,conteo):
    columna=8
    fila=random.randint(0,4)
    if cantidad_zombies==conteo:
        return 1,conteo
    elif oleada>=3:
        for x in range(0,5):
            if jardin[x][columna]=="🌱":
                colocar=random.randint(0,10)           
                if colocar in (3,5):
                    
                    
                    jardin[x][columna]="🧌"
                    vida_zom[(x,columna)]=zombies[2]["vida"]
                    conteo+=1
                elif colocar==4:
                    jardin[x][columna]="👹"
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

                                continue
                if jardin[fila][columna-1] in modelos_zombies:
                    pass
                elif jardin[fila][columna-1] in modelos_plantas:
                    print("El zombie se ha encontrado con una planta")
                    if jardin[fila][columna]=="🧟":
                        vida_plantas[(fila,columna-1)]-=zombies[1]["ataque"]
                    elif jardin[fila][columna]=="🧌":
                        vida_plantas[(fila,columna-1)]-=zombies[2]["ataque"]
                        
                    elif jardin[fila][columna]=="👹":
                        vida_plantas[(fila,columna-1)]-=zombies[3]["ataque"]
                        
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
    for i, j, contenido in casillas_explosion:
        jardin[i][j] = contenido
    jardin[fila][posicion] = "🌱"

    
    
#Pala: Para remover una planta de una casilla
def remover_planta(jardin,vida_plantas,modelos_plantas):
        pala_fila=int(input("Fila de la planta a eliminar: "))-1
        pala_columna=int(input("Columna de la planta a eliminar: "))-1
        if pala_fila not in range(5) or pala_columna not in range(9):
            print("\nEsta casilla no está en el tablero\n")
        elif jardin[pala_fila][pala_columna] in modelos_plantas:
            del vida_plantas[(pala_fila,pala_columna)]
            jardin[pala_fila][pala_columna]="🌱"
        else:
            print("Aquí no hay una planta")
            
#Para mostrar las estadisticas almacenadas de la partida           
def estadisticas_juego(estadisticas):
    stats=input("¿Deseas ver tus estadísticas? S/N:").upper().strip()
    if stats=="S":
        print("\nESTADÍSTICAS\n".center(38,"="))
        print(f'\nTurnos: {estadisticas["turnos"]}')
        print(f'Plantas: {estadisticas["plantas_colocadas"]}')
        print(f'Muertos: {estadisticas["zombies_eliminados"]}')
        print(f'Oleadas superadas: {estadisticas["oleadas_completadas"]}')
        print(f'Soles recolectados: {estadisticas["soles_recolectados"]}')
        print(f'Soles gastados: {estadisticas["soles_gastados"]}')
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
            explicacion_rapida()

        elif op_info == "2":
            explicacion_detallada()

        elif op_info == "3":
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
            plantas_rapido(plantas)

        elif op_plant == "2":
            plantas_detallado(plantas)

        elif op_plant == "3":
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
""")

    input("\nPresiona ENTER para volver...")


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

""")

    input("\nPresiona ENTER para volver...")


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
            zombies_rapido(zombies)

        elif op_zombie == "2":
            zombies_detallado(zombies)

        elif op_zombie == "3":
            break

        else:
            print("Opción inválida.")


def main_menu(plantas,zombies):
        
        while True:
            print("""
OPCIONES DEL MENÚ:\n
\t1-Jugar 🎮\n\t2-Intrucciones de cómo jugar 📖\n\t3-Información de plantas 🌻\n\t4-Información de zombies 🧟\n\t5-Salir 🚪
""")
            op=input("Elige una opciones: ")
            if op=="1":
                pvz(plantas,zombies)
            elif op=="2":
                instrucciones_juego()
            elif op=="3":
                mostrar_plantas(plantas)
            elif op=="4":
                mostrar_zombies(zombies)
            elif op=="5":
                print("Saliendo del programa...")
                return
            else:
                print("Opción no válida")
                

main_menu(plantas,zombies)

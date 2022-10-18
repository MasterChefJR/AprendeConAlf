import random
Aleatorio = random.randrange(0,2+1)   
juego = ["Piedra", "Papel", "Tijera"]
Tu = int(input(f'Elije entre una de las opciones\n1:{juego[0]}\n2:{juego[1]}\n3:{juego[2]}\n'))
print(f'Yo Elijo {juego[Aleatorio]}')
if Tu == 1:
    if Aleatorio == 1:
        print("Perdiste")
    elif Aleatorio == 2:
        print("Ganaste")
    else:
        print("Empate")
elif Tu == 2:
    if Aleatorio == 2:
        print("Perdiste")
    elif Aleatorio == 0:
        print("Ganaste")
    else:
        print("Empate")
elif Tu == 3:
    if Aleatorio == 0:
        print("Perdiste")
    elif Aleatorio == 1:
        print("Ganaste")
    else:
        print("Empate")
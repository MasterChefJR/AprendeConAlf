# El usuario adivina el numero
import random
Aleatorio = random.randrange(0,20)
x = True
while x:
    num = int(input("Inserta un numero: "))
    if  num == Aleatorio:
        print(f'Acertaste el numero es {Aleatorio}')
        break
    elif num > Aleatorio:
        print("Alto")
    elif num < Aleatorio:
        print("Bajo")



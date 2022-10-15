import random
Aleatorio = random.randrange(0,20)
# num = int(input("adivina el numero del 0 al 20: "))
# while (num != Aleatorio):
#     num = int(input("Inserta un numero: "))
#     if  num == Aleatorio:
#         break
# print(f'Acertaste el numero es {Aleatorio}')
print(f'El numero es ¿{Aleatorio}?')
Adivina = int(input("1.Si\n2.No\n"))
x = True
if Adivina == 2:
    while (Aleatorio != Adivina) == x:
        Aleatorio = random.randrange(0,20)
        print(f'El numero es {Aleatorio}')
        Adivina = int(input("1.Si\n2.No\n"))
        if Adivina == 1:
            x = False
            break
print(f'Acerte')
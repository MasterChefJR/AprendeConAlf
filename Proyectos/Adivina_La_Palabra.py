import random
# Tabla para los animales
# def hello():
#     with open("animales.txt") as a:
#         p = a.read()
#         return p
# DECLARAMOS LA LISTA DE LOS ANIMALES Y SELECCIONAMOS AL ANIMAL
x = random.randint(0,20)
animales = ["hog", "mole", "puppy", "beaver" ,"cow" , "kangaroo" , "koala" , "oryx", "lynx", "anteater", "parakeet", "aardvark", "squirrel", "elk", 
"crow", "gila monster", "pony", "horse", "musk deer", "walrus"]
animal = (animales[x])
largo = len(animal)
print(f'animal: {animal}\nPalabras: {largo}')
# ADIVINAMOS LA PALABRA DEL ANIMAL
    # continue
Vidas = 7
for i in range(0,Vidas):
    for x in range(0,largo):
        print(animal[x])
    nombre = input(f'Tienes {Vidas} Vidas Escribe Una Letra\n')
    if Vidas == 0 or len(nombre) >1:
        break
    elif nombre[0] != animal[x]:
        Vidas = Vidas-1
        print(f'Tienes {Vidas} Vidas Vuelve a intentarlo')
    elif nombre[0] == animal[x]:
        print(animal[x]+" s")

# while x:
#     palabra = input("Adivina el nombre del animal\nEscribe una letra: ")
#     contador = 0
#     vidas = 7
#     if (palabra != z[0]):
#         vidas -=1

#     elif vidas == 0:
#         print("Perdiste")
#         x = False
#     print(f'Te quedan {vidas} vidas')

#     if len(palabra) >1:
#         print("Solo una letra")
#         x = False
#     if palabra == z[contador]:
#         print(f'La palabra es {z[i]}')
#         contador +=1
# print(f'acertaste la palabra es {palabra}')
# Tabla para los animales
# def hello():
#     with open("animales.txt") as a:
#         p = a.read()
#         return p

# DECLARAMOS LA LISTA DE LOS ANIMALES Y SELECCIONAMOS AL ANIMAL
import random
x = random.randint(0,18)
animales = ["hog", "mole", "puppy", "beaver" ,"cow" , "kangaroo" , "koala" , "oryx", "lynx", "anteater", "parakeet", "aardvark", "squirrel", "elk", 
"crow", "pony", "horse", "walrus"]
animal = (animales[x])
largo = len(animal)
Vidas = 7
print(f'animal: {animal}\nPalabras: {largo}')
# ADIVINAMOS LA PALABRA DEL ANIMAL
# Terminar ciclo

while Vidas > 1:
    for i in range(0,largo):
        nombre = input(f'Tienes {Vidas} Vidas Escribe Una Letra\n')
        if nombre != animal[i]:
            print(animal[i])
            Vidas = Vidas-1
        elif nombre == animal[i]:
            respuesta = []
            respuesta.append(nombre)
            print(respuesta)
            if respuesta == animal:
                print("Ganaste")
        if Vidas == 0 or len(nombre) >1:
            break
    if Vidas == 0 or len(nombre) >1:
        break

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
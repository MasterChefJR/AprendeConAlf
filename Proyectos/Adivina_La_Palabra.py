import random
# def hello():
#     with open("animales.txt") as a:
#         p = a.read()
#         return p
x = random.randrange(0,20)
animales = ["hog", "mole", "puppy", "beaver" ,"cow" , "kangaroo" , "koala" , "oryx", "lynx", "anteater", "parakeet", "aardvark", "squirrel", "elk", "crow", "gila monster", "pony", "horse", "musk deer", "walrus"]
z = (animales[x])
x = True
for i in z:
    print(i,end=",")
print(z[0:len(z)])
palabra = "Hola Mundo"
while x:
    c = 6
    nombre = input("Escribe la palabra clave:")
    
    if nombre != palabra:
        c = c-1
        print(f'Te quedan {c}')
    if len(nombre) >1:
        x = False

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

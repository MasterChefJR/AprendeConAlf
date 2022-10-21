import random
# def hello():
#     with open("animales.txt") as a:
#         p = a.read()
#         return p
# DECLARAMOS LA LISTA DE LOS ANIMALES
x = random.randrange(0,20)
animales = ["hog", "mole", "puppy", "beaver" ,"cow" , "kangaroo" , "koala" , "oryx", "lynx", "anteater", "parakeet", "aardvark", "squirrel", "elk", 
"crow", "gila monster", "pony", "horse", "musk deer", "walrus"]
z = (animales[x])
# vISUALISAMOS LOS ANIMALES QUE SALGAN
for x in z:
    print(x,end=",")
print(z[0:len(z)])
nombre = ''
# ADIVINAMOS LA PALABRA DEL ANIMAL
x = True
while x:
    c = 7
    if nombre != z[x]:
        for i in range(0,7):
            if nombre == z[x]:
                print(f'Correcto {nombre} Tienes {c} vidas')
            elif nombre != z[x]:
                c = c-1
            nombre = input("Escribe la palabra clave:")
            print(f'Te quedan {c} vidas')
    if c == 0 or len(nombre) >1:
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

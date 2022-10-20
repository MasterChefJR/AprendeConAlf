import random

def hello():
    with open("adibina.txt") as a:
        p = a.read()
        return p
print(hello())
x = True
while x:
    palabra = input("Escribe una letra")
    if len(palabra) >1:
        print("Solo una letra")
    elif len(palabra) == 1:
        print(f'Elejiste {palabra}')
        x = False
print(f'acertaste la palabra es {palabra}')        

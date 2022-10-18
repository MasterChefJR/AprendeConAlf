# file = open("Adivina.txt", "r")
# cont = file.read()
# print(cont)
# file.close()


# with open('Adivina.txt') as a:
#     contenido = a.read()
#     print(contenido)

f = open ('Adivina.txt','r')
mensaje = f.read()
print(mensaje)
f.close()
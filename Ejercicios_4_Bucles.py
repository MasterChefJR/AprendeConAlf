# Ejercicios de Bucles

"""Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

Palabra = input("Palabra: \n")
for i in range(10):
    print(Palabra)
"""
"""Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

Edad = int(input("Edad: "))
for i in range(1,Edad+1):
    print(f'Tienes {i} años')
"""
"""Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

Numero = int(input("Numero: "))
for i in range(1, Numero+1, 2):
    print(i, end=", ")
"""

"""Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

Numero = int(input("Numero: "))
for i in range(Numero, -1, -1):
    print(i, end=", ")
"""
"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

"""Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****

Numero = int(input("Numero: "))
for i in range(Numero+1):
    print("*"*i)
"""
"""Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

Numero = int(input("Tabla de Multiplicar: "))
for i in range(1,10+1):
    print(f'{Numero} * {i} = {Numero*i}')
"""
"""
Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

Numero = int(input("escribe un numero: "))
for i in range(1,Numero+1, 2):
    for j in range(i, 0,-2):
        print(j, end=" ")
    print("")
"""
"""
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contrasenia = input("Contraseña: ")
password = "cacahuate"
while contrasenia != password:
    contrasenia = input("Contraseña: ")
print(f"Su contraseña es: {contrasenia}")
"""
"""
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

n = int(input("Numero: "))
v = True
for i in range(2,n):
    if n % i == 0:
        print(f'{n} No Es Primo')
        v = False
        break
if v:
    print(f'{n} Es Primo')
"""
"""Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Palabra: ")
for i in range(len(palabra)-1,-1,-1):
    print(palabra[i])
"""
"""
Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

"""
Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""


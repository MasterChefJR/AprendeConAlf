# Ejercicios de Listas y Tuplas
"""
Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
Materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
print(Materias)
"""

"""
Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio 
<asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

Materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
for i in range(len(Materias)):
    print(f'Yo estudio {Materias[i]}.')
"""
"""
Ejercicio 3

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario.

Materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
Total = []
for i in range(0,(len(Materias))):
    Nota = int(input(f'¿Que nota sacaste en {Materias[i]}? '))
    Total.append(Nota)
for j in range(len(Materias)):
    print(f'Sacaste en {Materias[j]}: {Total[j]}')
"""

"""
Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

Total = int(input("¿Cuantos numeros tiene la loteria?  \n"))
Ganadores = []
for i in range(Total):
    Loteria = int(input("Voletos ganadores: "))
    Ganadores.append(Loteria)
    Ganadores.sort()
print(Ganadores)
"""

"""
Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

Numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Numeros.reverse()
print(Numeros)
"""

"""
Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

Materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
Total = []
for i in range(0,(len(Materias))):
    Nota = int(input(f'¿Que nota sacaste en {Materias[i]}? '))
    Total.append(Nota)
for j in range(len(Materias)):
    if Total[j] <= 5 and Total[j]>= 0:
        print(f'Sacaste en {Materias[j]}: {Total[j]} Materia por Repetir')
    else: 
        print(f'Sacaste en {Materias[j]}: {Total[j]} Materia Pasada')
"""

"""
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0, len(abecedario), 3):
    if i % 3 == 0:
        print(abecedario[i].split(','), end=" ")
"""
"""
Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
Palindromos " Son palabras que son iguales de derecha a izquierda y de izquierda a derecha, ejemplo= "radar, oso, reconocer, ala"

Palabra = input("Palindromo: ")
Palabra_Reversa = Palabra
Palabra = list(Palabra)
Palabra_Reversa = list(Palabra_Reversa)
Palabra_Reversa.reverse()
if Palabra == Palabra_Reversa:
    print("Palindromo")
else:
    print("No es palindromo")
"""

"""
Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
Nombre = input("Escribe una palabra: ")
vocabulario = ["A","E","I","O","U"]
for i in range(len(vocabulario)):
    for j in Nombre:
        print()



"""
Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
"""
"""
Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""
"""
Ejercicio 12
Escribir un programa que almacene las matrices
 A = (1 2 3)   y  B =  (-1 0)
     (4 5 6)            (0 1)
                        (1 1)
                        
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
""" 

"""
Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""
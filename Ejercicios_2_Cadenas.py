# Ejercicios de Cadenas
"""Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario
tantas veces como el número introducido.

Nombre = input("Nombre: ") + "\n"
Repetir = int(input("Veces que repetira: "))
print(Nombre*Repetir)
"""
"""Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces,
una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

Nombre = input("Nombre: ")
print(Nombre.lower())
print(Nombre.upper())
print(Nombre.title())
"""

"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> 
letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

Nombre = input("Nombre: ")
print(f'{Nombre} tiene  {len(Nombre)} de letras')
"""
"""Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos 
dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de 
teléfono sin el prefijo y la extensión.

Telefono = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print(f'El número de teléfono es  {Telefono[4:-3]}')
"""
"""Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

Frase = input("Frase: ")
print(f'Frase invertida de {Frase} es {Frase[::-1]}')
"""

"""Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la 
vocal introducida en mayúscula.

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))
"""

"""Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.

Correo = input("Introduce tu correo electrónico: ")
print(Correo[:Correo.find('@')] + '@ceu.es')
"""

"""Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número 
de céntimos del precio introducido.

precio = int(input("Escrube una cantidad en centimos: "))
print(f'Escribio {precio} y en euros serian {precio/10}')
"""


"""Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar 
el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
print(f'Día {fecha[:2]}')
print(f'Mes {fecha[3:5]}')
print(f'Año {fecha[6:]}')
"""

"""Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los 
productos en una línea distinta.

cesta = input('Introduce los productos separados por comas: ')
print(cesta.replace(',', '\n'))
"""


"""Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del 
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros 
y 2 decimales.

producto = input("Producto: ")
precio = float(input("Precio: "))
unidades = int(input("Unidades: "))
print(f'Producto: {producto}, Precio: {precio}, Unidades: {unidades}\nTotal: {precio*unidades}')
"""

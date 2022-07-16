# Ejercicios de Tipos de Datos Simples
"""Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")
"""
"""
Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

Palabra = "¡Hola Mundo!"
print(Palabra)
"""


"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena 
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

Nombre = input("Nombre: ")
print(Nombre)
"""

"""Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética  ((3+2)/(2*5))*2

print(((3+2)/(2*5))**2)
"""


"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le 
corresponde.

Hora = int(input("Horas Trabajadas: "))
Costo_Hora = int(input("Precio por Hora: "))
print(f'Hoy Ganaste: {Hora*Costo_Hora}')
"""

"""Ejercicio 6
Escribir un programa que lea un entero positivo "n" , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta.
La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma: suma=n(n+1)/2

n = int(input("Escribe un entero positivo: "))
suma=n*(n+1)/2
print(f'La suma de 1 al {n} = {suma}')
"""


"""Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

kg = int(input("peso en kg: "))
mts = float(input("altura en metros: "))
imc = kg/(mts*mts)
print(f'Sun indice de masa corporal es de: {imc}')
"""
"""Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input("numero: "))
m = int(input("numero: "))
print(f'{n} entre {m} da un cociente de {n//m} y un resto de {n%m}')
"""
"""Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en
la inversión.

cantidad = float(input("Cantidad a invertir: "))
Interes_Anual = float(input("Interes Anual: "))
Tiempo = int(input("Numero de Años: "))
inversion = (cantidad*(Interes_Anual/100+1)**Tiempo)
print(inversion)
"""

"""Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular
el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.

Payaso_Vendidos = int(input("payasos Vendidos: "))
payaso = 112*Payaso_Vendidos
Monas_Vendidas = int(input("Muñecas Vendidas: "))
Monas = 75*Monas_Vendidas
print(f'Se Vendieron {Payaso_Vendidos} payasos y {Monas_Vendidas} Muñeas \npeso total = {payaso+Monas} gr')
"""

"""Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al 
balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa 
debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

interes = 4/100
Deposito = float(input("Inversion: "))
Frist_Year = Deposito*(1+interes)
print(Frist_Year)
Two_Year = Frist_Year*(1+interes)
print(Two_Year)
Three_Year = Two_Year*(1+interes)
print(Three_Year)
"""
"""Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del 
día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barras = int(input("Barras Vendidas: "))
precio = 3.49
descuento = 60/100
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")
"""
print("hola")
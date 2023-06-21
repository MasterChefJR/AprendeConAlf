# Ejercicios de Tipos de Datos Simples
"""Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
Respuesta:
print("¡Hola Mundo!")
"""
"""
Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
Respuesta:
Variable = "¡Hola Mundo!"
print(Variable)
"""
"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena 
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
Respuesta: 
Nombre = input("Nombre: ")
print(f'¡Hola {Nombre}:D!')
"""



"""Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética  ((3+2)/(2*5))*2
Respuesta: 
print(((3+2)/(2*5))**2)
"""
"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le 
corresponde.
Respuesta: 
Horas_Trabajadas = int(input("Horas trabajadas: "))
Pago = int(input("Pago Por Horas trabajadas: "))
print(Pago*Horas_Trabajadas)
"""
"""Ejercicio 6
Escribir un programa que lea un entero positivo "n" , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta.
La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma: suma=n(n+1)/2
Respuesta: 
n = int(input("Numero: "))
print(n*(n+1)/2)
"""


"""Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y 
muestre por pantalla la frase Tu índice de masa corporal es 
<imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso / altura**2
Respuesta:
kg =  int(input("Kilos que pesas: "))
mts = float(input("Altura en metros: "))
idmc = kg/(mts*mts)
print(f'Tu IMC es: {round(idmc,2)}')
"""

"""Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> 
donde <n> y <m> son
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input("numero 1: "))
m = int(input("numero 2: "))
c = n/m
r = n%m
print(f'resto= {c}\nresiduo = {r}')
"""

"""Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión.

capital = int(input("capital: "))
interes_Anual = float(input("Interes anual: "))
anios = int(input("años invertidos: "))
# print(f'total= {capital*(interes_Anual/100+1)**anios}')
print(f'total: {(capital*(interes_Anual/100+1)**anios)}')
"""

"""Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular
el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.

payasos_Vendidos = int(input("Payasos vendidos: "))
Muñecas_Vendidos = int(input("Muñecas vendidas: "))
print(f'Total de Peso Payasos vendidos: {payasos_Vendidos*112}g\nTotal de Peso Muñecas vendidas: {Muñecas_Vendidos*75}g')
print(f'Total = {(payasos_Vendidos*112)+Muñecas_Vendidos*75}g')
"""

"""Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al 
balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa 
debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

dinero_depositado = int(input("Dinero depositado: "))
interes_anual = 1.04
Primer_pago =dinero_depositado*interes_anual
print(f'Primer año: {round(Primer_pago, 2)}')
Segundo_pago =Primer_pago*interes_anual
print(f'Segundo año: {round(Segundo_pago,2)}')
tercer_pago =Segundo_pago*interes_anual
print(f'Tercer año: {round(tercer_pago,2)}')
"""

"""Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del 
día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

pan = 3.49
Pan_Vendido = int(input("Barras Vendidas que no son del dia: "))
total = pan*Pan_Vendido
print(f'Precio habitual del pan: {pan}€')
print("Descuento por no ser fresca: 60%")
print(round(total*(1-60/100),2))
"""
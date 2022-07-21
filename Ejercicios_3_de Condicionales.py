# Ejercicios de Condicionales
"""Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Edad: "))
if edad >=18:
    print("Eres Mayor de edad")
else:
    print("Eres menor de edad")
"""

"""Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contra = "angel"
password = input("Contraseña: ")
if password == contra:
    print("correcta")
else: 
    print("Error")
"""

"""Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input("Numero dividendo: "))
num2 = int(input("Numero divisor: "))
if num2 == 0:
    print("error")
else: print(num1/num2)
"""

"""Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Numero: "))
if numero % 2 == 0:
    print("es par")
else: print("es impar")
"""

"""Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y 
sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Edad: "))
Ingreso = float(input("Ingreso Mensual: ")) 
if edad > 16 and Ingreso >= 1000:
    print("Deves trivutar")
else: print("no deves trivutar")
"""

"""Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("ingresa tu nombre: ")
nombre.lower()
Sexo = input("M o H: ")
Sexo.lower()
if (nombre[0] <= 'm') and (Sexo == 'm'):
    print("Grupo A")
elif nombre[0] >= 'N':
    print("Grupo B")
"""

"""Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

renta = float(input("Renta anual: "))
cantidad = [0,10000,20000,35000,60000]
if renta >= cantidad[0] and renta <  cantidad[1]:
    print("Pagas el 5%")
elif renta >= cantidad[1] and renta < cantidad[2]:
    print("Pagas el 15%")
elif renta >= cantidad[2] and renta <  cantidad[3]:
    print("Pagas el 20%")
elif renta >= cantidad[3] and renta <=  cantidad[4]:
    print("Pagas el 30%")
elif renta > cantidad[4]:
    print("Pagas el 45%")
"""
"""Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en 
mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una
tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

Puntos = float(input("Puntos conseguidos: "))
Salario = 2400
Rendimiento = ["Insuficiente", "Aceptable", "Meritorio"]
if Puntos >= 0 and Puntos < 0.4:
    Rendimiento = Rendimiento[0]
elif Puntos >= 0.4 and Puntos < 0.6:
    Rendimiento = Rendimiento[1]
elif Puntos >= 0.6 and Puntos:
    Rendimiento = Rendimiento[2]
print(f'Su bono total = {(Puntos+1)*Salario}\n{Rendimiento}')
"""



"""Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ 
y si es mayor de 18 años, 10€.

Edad = int(input("Edad: "))
Precios = "Gratis"
if Edad >=4 and Edad < 18:
    Precios = "5 Euros"
elif Edad >=18:
    Precios = "10 Euros"
print(f'Costo: {Precios}')
"""

"""Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se 
puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los 
ingredientes que lleva.


# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Ingredientes = ["Tomate", "Mozzarella"]
Eleccion = input("Desea una pizza vegetariana [Y] o [N] \n")
Eleccion = Eleccion.upper()
if Eleccion[0] == 'Y':
    Pizza_Vegetariana = ["Pimiento", "Tofu"]
    Eleccion_Vegetariana = int(input(f'Seleccione un Ingrediente\n1- {Pizza_Vegetariana[0]}\n2- {Pizza_Vegetariana[1]}\n'))
    if Eleccion_Vegetariana == 1:
        Ingredientes.append(Pizza_Vegetariana[0])
    elif Eleccion_Vegetariana == 2:
        Ingredientes.append(Pizza_Vegetariana[1])
    else:
        Ingredientes = ""
        print("Error, intente de nuevo")
elif Eleccion[0] == 'N':
    Pizza_Clasica = ["Peperoni", "Jamon", "Salmon"]
    Eleccion_Vegetariana = int(input(f'Seleccione un Ingrediente\n1- {Pizza_Clasica[0]}\n2- {Pizza_Clasica[1]}\n3- {Pizza_Clasica[2]}\n'))
    if Eleccion_Vegetariana == 1:
        Ingredientes.append(Pizza_Clasica[0])
    elif Eleccion_Vegetariana == 2:
        Ingredientes.append(Pizza_Clasica[1])
    elif Eleccion_Vegetariana == 3:
        Ingredientes.append(Pizza_Clasica[2])
    else:
        Ingredientes = ""
        print("Error, intente de nuevo")
else:
    Ingredientes = ""
    print("Error, intente de nuevo")
print(f'pizza: {Ingredientes}')
"""

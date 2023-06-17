# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
# líneas distintas el nombre del usuario tantas veces como el número introducido.

# Name = input("Nombre: ")
# x = "\n"
# Numero = input("Escribe un numero: ")
# print(f'{str(Name+x)*int(Numero)}')

# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre 
# completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera 
# letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

Pregunta_Nombre = input("Nombre: ")
print(f'Mayusculas: {Pregunta_Nombre.upper()}')
print(f'Minusculas: {Pregunta_Nombre.lower()}')
print(f'Primera Letra Mayusculas: {Pregunta_Nombre.title()}')

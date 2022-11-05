

# Bucle while 

# un Bucle while que significa mientras que se cumpla una determinada condicion
""" 
numero = 0
# numero es igual a 0. 0 es menor que 20?si.(lo que le damos es una condicional) si 20 es menor a 0 quiero que imprima las veces que pueda 
while numero <20:
    print(numero)
    # le digo que sume igual 1
    numero += 1
"""

import math 

numero=int(input("Escribe un numero: "))

while numero <0:
    print("porfavor ingrese un numero positivo: ")
    numero = int(input("vuelva a ingresar un numero positivo: "))
print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero):.2f}") # para sacar la raiz se tiene que agregar el (math.sqrt)



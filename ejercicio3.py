
#Ejercicio 3 Obtener el radio y longitud de un circulo en Python

""" math lo vamos a ocupar para trabajar operaciones pi """

import math 

r=float(input("Ingrese el radio: "))
area = math.pi*r**2
longitud = 2*math.pi*r

# como agregar la cantidad de decimales que queremos :.2f
print(f"su area es de: {area:.1f}")
print(f"su longitud es de: {longitud:.2f}")
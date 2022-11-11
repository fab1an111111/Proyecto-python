

#Bucle for

# i vamos a recorrer datos in(en)[ ]. es decir que mi variable va a sacar toda los datos 
""" 
for i in [6,8,9,4,7]:
    print(f"objeto: {i}")

"""
# claro ejemplo de como pedir informacion
""" 
data = [6,5,3,8,"hola"]

for i in data:
    print(f"objeto {i}")
"""

# ejercicio 1 
# Crear un programa que muestre la sumatoria de todos los numeros entre el 0 y el 100

total = 0 
# la funcion rango, el rango(range) lo puedes a tomar entre un numero inicial y un numero final
# el bucle recorrera un rango de 0 a 101
for i in range(101):
    total = total+i
    print("sumatoria: ",total)

# formula de como se trabaja, el (nf-1, es por que le esta restando un numero), ej: un rango recorrera del numero 0 al 101 (el 101 se resta -1)
# rango 0,1,2......100 (nf-1)
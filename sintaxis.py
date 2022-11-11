
#Hola soy un comentario >> comentarios con (#)
# import math >> Importacion de modulos (import)

# def codigo369(): >> Funiones definidas cond (def), las funciones se definen con un def es crear una funcion que va a definir el ejercicio

# for i in range(0,n-1) >> Bucles con (rangos)

# dato ="codigo369" >> en python no se utilizan las palabras reservadas,si es que va hacer de tipo int,string,double,byte.no se necesita.

# print(f"hola mundo {dato}") imprime salida de datos en consola 


# 1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio

n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))

def max (n1,n2):
    if n1 < n2:
     print(n2)
    elif n2 < n1:
     print(n1)
    else:
     print("son iguales")

# 2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.


""" 
numeros = max(3,56,7)
print(numeros) 
"""

# 3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
""" 
import math 

longitud = [10,20,30]

a = 2*math.pi*longitud

print(a)
 """
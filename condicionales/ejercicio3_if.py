
# ejercicio 3 

""" crear un programa que compare dos nombres, y verificar si hay coincidencia o no, si es que 
ambos nombres comienzan con la misma letra o si termina con la misma letra """


""" 
nombre = input("primer nombre: ")
nombre2 = input("segundo nombre: ")

if nombre == nombre2:
    print("el nombre es igual")
elif nombre != nombre2:
    print("son nombres distintos")     

 """




nombre1 = input("primer nombre: ")
nombre2 = input("segundo numero: ")

# python maneja indices para ubicar las letras en que parte estan (siempre se empieza a contar desde el 0), con (-1) obtenemos la ultima letra de las palabras
if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("hay considencia")
else:
    print("no hay considencia")
   



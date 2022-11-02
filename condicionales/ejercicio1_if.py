
#ejercicio 1 

#crear un programa que pida 2 numeros y obtenga como resultado cual es par o si ambos lo son 

""" 
n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese segundo numero: "))

# le digo si es un es 10 el modulo(%)lo divide en 2 si se arroja un 0 es par
if n1%2 == 0 and n2%2 == 0:
    print("ambos son pares")
elif n1%2 == 0 and n2%2 != 0:
    print(f"{n1} es un numero par")
elif n1%2 !=0 and n2%2 == 0:
    print(f"{n2} es un numero par")
else:
    print("ninguno numero es par")

 """

numero1 = int(input("primero numero: "))
numero2 = int(input("segundo numero: "))

if numero1%2 == 0 and numero2%2 ==0:
    print(f"{numero1} es un numero par")
    print(f"{numero2} es un numero par")
elif numero1%2!= 0 and numero2%2!= 0:
    print(f"{numero1} no es par")
    print(f"{numero2} no es par ")
else:
    print("no hay numero encontrados");

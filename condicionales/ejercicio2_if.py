
# ejercicio 2 

# crear un programa que pida 3 numeros y determine cual es mayor

""" n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
n3 = int(input("numero 3: "))

# aqui le digo que el numero n1 tiene que ser mayor o igual a numero 2 y numero 3 
if n1>=n2 and n1>=n3:
    print(f"el numero mayor es: {n1}")
elif n2>=1 and n2>=n3:
    print(f"el numero mayor es: {n2}")
elif n3>=n1 and n3>=n2:
    print(f"el numero mayor es: {n3}") """



numero1 = int(input("primer numero: "))
numero2 = int(input("segundo numero: "))
numero3 = int(input("tercer numero: "))

if numero1 <= numero2 and numero1 <= numero3:
    print(f"el primer numero es menor ")
elif numero2 <= numero1 and numero2 <= numero3:
    print(f"el segundo numero es menor")
elif numero3<= numero1 and numero3<= numero2:
    print("el tercer numero es menor")
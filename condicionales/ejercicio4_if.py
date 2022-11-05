

#ejercicio 4 

# Crear un programa que simule un cajero automatico con un saldo inicial de $ 2000, con el siguiente menu:
"""
1. Ingreso de dinero
2. Retirar dinero 
3. Mostrar dinero 
4. salir  

"""

saldo = float(2.000)

print("1. Ingreso de dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. Salir")

seleccion = int(input("elija un numero: "))

if seleccion == 1: 
    ingreso = float(input("ingrese su monto: "))
    saldo+=ingreso
    print(f"Nuevo saldo en la cuenta: {saldo}")
elif seleccion == 2:
    retiro = float(input("cuanto quiere retirar: "))
    if retiro>saldo:
        print("saldo es insuficiente")
    else:
        saldo-=retiro
        print(f"su retiro es de: {saldo}")

elif seleccion == 3:
    print(f"saldo disponible {saldo}")
    
elif seleccion == 4:
    print("salir")
else:
    print("error de entrada de datos")

    


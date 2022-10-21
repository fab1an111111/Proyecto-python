
""" imprime un mensaje 

print ("hola mundo")
print("soy fabian") 

"""

""" tipos de textos son los textos tipo string, numberos y boleanos 

tipo de dato int 
numero = 1;

tipo de dato float 
numero2 = 1.2;

 tipo de dato string 
nombre = "fabian";
"""


""" no es necesario darle un dato a las varaibles como int(js) """
""" print (nombre);  """

""" print(numero);  """

""" la funcion type sirve para indicar de que tipo de variable es 
 print(type(numero)); """

""" hacer una cadena de caracteres
palabra ="snopdog";

print(palabra); """



""" hacer datos de tipo boleanos (True,False)"""
""" dato = False
print(dato);
print(type(dato))
 """


""" como hacer suma 
numero1 = 2;

numero2 = 4;

suma = numero1 + numero2;

ejercicio = (numero1 +numero2*5)/12

print((type)suma);
"""


""" como combinar un string con un numero 
n1=50;

n2=24;

resultado = (n1 + n2*4)/12

print("es igual a =" , resultado)

"""


""" OPERCAIONES ARITMETICAS 

OPERADOR    DESCIPCION             EJEMPLO     RESULTADOR
+           Suma                    c=3+5       c=8
-           Resta                   c=6-4       c=2
-           Negacion                c=-9        c=-9
*           Multiplicacion          c=3*9       c=27
**          Potencia                c=2**3      c=8
/           Division                c=7/2       c=3.5
//          Division entera         c=7//2      c=3
%           Modulo                  c=9%3       c=0


n1 = 12
n2 = 3
c = n1%n2;

print("el valor es:", c);
 """


""" ejemplos de formulas 
 
r = (5+9/3)**2
print(r)
"""



""" OPERADORES RELACIONALES 


OPERADOR    COMPARACION

==          Igual que 
!=          Distinto que 
<           Menos que 
<=          Menor o igual que
>           Mayor que 
>==         Mayor o igual que    

"""

""" 
r = 100 >= 120

print(r)
 """


""" 

OPERADORES LOGICOS

Operador        Descripcion

and             Se cumple a y b

or              Se cumple a o b

not             No a 

"""

""" a = 30; 
b = 40;
c = 50;

r = ((a<b) or (b>c) )

print(r);
 """

""" lo que hacemos es que la misma variable su sume pero aumentado en 1 """
c = 0;
c += 10;
""" restamos 5  """
c -= 5;
""" se incrementa con una multiplicacion 
c *= 3;

"""
""" dividemos 
c /= 5;

"""

""" potenciamos  

c **= 3;
"""

""" modulo 

c %= 3;

print(c);

"""



""" salida de datos 

esta es la forma mas comun de hacr salida de datos 

app = "flutter"
proyecto = "comFlu"
print(f"se hara en {app} se llamara {proyecto}");

"""


""" ENTRADAS DE DATOS """

""" para pedir datos al usuario es input 
entran datos y salen datos 

cadena = input("¿como se llama tu proyecto?: ")
print(f"Tu proyecto se llama {cadena}")

"""


""" en phython no se pueden mesclar los string con los numeros 
cadena = input("¿que version es: ")
print(f"es la version: {cadena+1}")
"""


""" forma correcta 
cadena = int (input("¿que version es?: "))
print(f"es la version: {cadena+1}")
"""


""" forma de hacer con decimales """

cadena2 = float(input("que version es?: "))
print(f"es la version: {cadena2+ 1.3}")
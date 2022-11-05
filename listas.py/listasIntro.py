

# para crear listas solo vastara en agregar dos corchetes [ ]

#introduccion a listas, se puede agregar cualquier tipo de lista
""" 
array = ["futbol","pc",18.6,10,[6,7,10,4],True,False]
# en python se suele agregar con enumeraciones desde el 0 asia delante, para agregar el ultimo dato es desde el -1 ...
# imprime desde el 0 al 2 ,
print(array[1:2])

#  puede sacar datos
print(array[2:])
"""

# el array lo podemos almacenar manual mente 
# esto se almacenaria en una base de datos con una tabla 
""" 
array = ["nombre","apellido","rut","correo"]

print(array[1])
"""

# la funcion (len) nos ayudara a contar la cantidad de datos que tenemos en este caso comienza contando desde el 1
""" 
array = ["futbol","pc",18.6,18,[6,7,10,4],True,False]

print(len(array))
 """

# la funcion (append) agrega a la ultima valor uno mas es decir que agregaria una adiccional 
""" 
array = ["juan","pedro","jorge","ana","jose"]
array.append("pepe")
array.append("fabian")
# funcion para insertar datos (siempre tienes que agregar el indice)
array.insert(1,"goku") 
#la funcion (extend) nos servira para agregar todos los datos al final
array.extend([1,66,"hola",False])

print(array)
"""

# como concadenar una lista 
array1 = ["messi","cr7",18.6,10,[1,2,3,4],False,True,]
array2 = [200,250,"hola"]

array3 = array1 + array2
# para buscar un determinado valor en las listas(arrays) valor que buscas y su determinado lista,este nos dara un valor boleano si es que se encuntra en dicho array 
# print(200 in array2)
# numero de index(ubicacion) y valor que busco esta empezaria a contar desde 0
#print(array1.index(10))

#la funcion(count) nos dira cuantas veces se repetira un valor 

#print(array1.count("messi"))

#como eliminar valores de las listas(array), con (remove) le diremos que valor queremos retirar
""" 
array1.remove("messi")
print(array1)

"""

#como limpiar listas(array), con (clear) se borra todos los valores de la lista
""" 
array1.clear()
print(array1)
"""

# la funcion (reverse) nos servira para cambiar la posicion de los datos 
""" 
array1.reverse()
print(array1)
"""

arrayNumeros = [1,2,8,-11,5]
# la funcion (sort) nos ayudara a ordenar los datos de forma ascendiente(de menos a mayor ) 
#arrayNumeros.sort()
#print(arrayNumeros)

# como hacerla de forma descendente agregaremos la funcion(reverse)

arrayNumeros.sort(reverse=True)
print(arrayNumeros)


"""  Ejercicio 4 Obtener el precio final que se tiene que pagar si se aplica el 36%
de descuento del total de la compra. """



precio = float(input("producto: "))

#como aplicar descuentos(se agregar el descuento que quieras mas la unidad dividido por 100%)
#se puede aplicar tambien de forma 36% sobre 100% (36/100)
descuento = precio*(36/100)

precioFinal = precio-descuento

print(f"el precio final es: $/ .{precioFinal:.3f}")

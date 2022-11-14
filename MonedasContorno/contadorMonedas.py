

import cv2 
# (numpy) modulo default de python, esta libreria nos ayudara a trabajar con informatica cientifica 
import numpy as np

# los valores siempre tienen que ser impares o generara errores, las matrices trabajan con numeros pares
valorGauss = 1
valorKernel = 30

original = cv2.imread('monedas2.jpg')
gris = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
# modelado(GaussianBlur) podemos ocuparlo cuando tengamos imagenes borrosas link:https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
# desenfoque gausseano, los valores siempre tienen que ser de tipo igual ej:(3,3) o (hola,hola) 
gauss = cv2.GaussianBlur(gris,(valorGauss,valorGauss), 0)
# la funcion(Canny) nos ayudara a eliminar los ruidos que quedan, link:https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
canny = cv2.Canny(gauss,60,100)

# en el modelado kernel sera necesario ocupar matrices (()),(uint8) enteros con 8 byte estos pueden entregar valores de tipo doble
kernel = np.ones((valorKernel,valorKernel),np.uint8)
# funcion (morpho) o transformaciones morfologicas link: https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
# esta morphologya nos ayudara a cambiar la forma 
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE,kernel)

contornos, jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# la funcion (len) nos permitira contar los caracteres de la cadena 
print("monedas en contradas: {}".format(len(contornos)))
# se agrega todo los contornos y dibuja todo los contornos en la imagen original
cv2.drawContours(original,contornos,-1,(0,0,255),2)


#mostrar resultados
cv2.imshow("grises",gris)
cv2.imshow("gauss",gauss)
# eliminar los ruidos para encontrar contornos
cv2.imshow("canny",canny)
cv2.imshow("cierre",cierre)
cv2.imshow("Resultado", original)
cv2.waitKey(0)

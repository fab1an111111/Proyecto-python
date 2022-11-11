

#Contornos 
#Los contornos son un conjunto de cordenadas que nos servira para indentificar una determinada area 
# las imagenes se dividen en tres canalas R,G,B estos se representan con numeros

# importando OpenCv y saber la version 
""" 
import cv2
print(cv2.__version__) 
"""

import cv2

""" 
# leer la imagen con(imread) 
imagen = cv2.imread('contorno.jpg')
# mostrar imagen con(imshow)
cv2.imshow("imagen")
# funcion (waiKey) nos sirve para decirle a python que no cierre su ventanilla emergente  
cv2.waitKey(0)
# destruir todas las ventanas abiertas 
cv2.destroyallwindows()
 """

""" 
img = cv2.imread("doge.jpg")
# Funcion cvtColor  link:https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html
# escala de grises
grises = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("imagen original", img)
cv2.imshow("imagen en gris", grises)
cv2.waitKey(0)
cv2.destroyallwindows()
"""



img2 = cv2.imread("doge.jpg")
grises = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# threshold = Umbral simple, separar nuestro objeto de su entorno  link:https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html)
# este metodo devuelve dos salidas.El primero es el umbral que se utilizo y el segundo resultado es la imagen umbralizada, funcion(-,) adopta una variable fictica que no existe o simplementa agrega otra variable
_,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
# la funcion (findContours) nos ayudara a obtener los contornos link:https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
# cv2.RETR_LIST nos ayudara a hacer una lista de datos 
contorno,jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]
#funcion(drawContours) dibujar contorno,link:https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
cv2.drawContours(img2,contorno,-1,(182, 131, 48),3)

cv2.imshow("imagen original", img2)
#cv2.imshow("imagen en gris", grises)
#cv2.imshow("imagen umbral", umbral)
cv2.waitKey(0)
cv2.destroyallwindows()



""" 
para dibujar todos los contornos en una imagen, se agrega la imagen y su contorno, para agregar todos los contornos se agrega el -1,luego se agrega los colores, despues se agrega el
grosor que quiera  """
# cv.drawContours(img2,contours, -1,(0,255,0)3)
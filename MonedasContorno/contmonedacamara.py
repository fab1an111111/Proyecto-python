

# contar monedas por camara


import cv2 
import numpy as np

def ordenarpuntos(puntos):
    # funcion (concatenate) nos ayuda a enlasar matrices para dejarlas en una sola, las matrices comienzan desde el 0
    n_puntos = np.concadenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist()
    # funcion (sorted) nos ordenara los puntos,cuando concatenamos estas listas suelen estar desordenadas ahi es cuando dentra esta funcion 
    # la funcion (key) asume el tipo de orden para dar a las matrices. # funcion(lambda) reconocera el orden que queremos ordenar (0-1 = 0)
    y_order = sorted(n_puntos,key=lambda n_puntos: n_puntos[1])
    # hace un recorrido desde el punto[0] al punto[1]
    x1_order = y_order[:2]
    #recorre el punto[0]
    x1_order = sorted(x1_order, key=lambda x1_order:x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order,key=lambda x2_order:x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

#alinear el molde de imagenes, nos servira por si estamos apuntado con el celular o moviendolo, para que se vea igual si esta quieta 

def alineamiento(imagen,ancho,alto):
    imagen_alineada = None
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    tipoumbral, umbral = cv2.threshold(grises,150,255, cv2.THRESH_BINARY)
    cv2.imshow("Umbral",umbral)
    # le agrego [0] para que centre y se aplique todo 
    contorno = cv2.findContours(umbral,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # (reverse) nos ordenara las parte de los puntos de mayor a menores
    contorno = sorted(contorno, key=cv2.contourArea,reverse=True)[:1]
    for c in contorno:
        #la funcion (arcLength)nos ayudara a encontrar el centro de la masa del objeto y el area link:https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
        # con epsilon le bajamos la frecuencia de las curvas 
        epsilon = 0.01*cv2.arcLength(c,True)
        aproximacion=cv2.approxPolyDP(c,epsilon, True)
        if len(aproximacion) == 4:
            puntos = ordenarpuntos(aproximacion)
            # datos de ancho y altura
            puntos1 = np.float32(puntos)
            puntos2 = np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            # metodo de perspectiva(darvueltas o mover el celular)
            M = cv2.getPerpectiveTransform(puntos1, puntos2)
            imagen_alineada = cv2.wardPerspective(imagen, M,(ancho,alto))  
    return imagen_alineada
#captura de video 
capturavideo = cv2.VideoCapture(0)       

while True:
    tipocamara,camara = capturavideo.read()
    if tipocamara == False:
        break
    imagen_A6 = alineamiento(camara,ancho=480,alto=640)
    if imagen_A6 is not None:
        puntos = []
        image_gris = cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(image_gris,(5,5),1)
        # se trabaja con dos procesos de indemnizaciones para estas imagenes de video 
        _,umbral2 = cv2.threshold(blur,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("umbral",umbral2)
        contorno2 = cv2.findContours(umbral2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6,contorno2, -1, (255,0,0),2)
        suma1 = 0.0
        suma2 = 0.0
        for c2 in contorno2:
            area = cv2.contoursArea(c2)
            Momentos = cv2.moments(c2)
            # mometos estaticos(m00"espaciales"")
            if(Momentos["m00"]==0):
                Momentos["m00"]=1.0
            x=int(Momentos["m10"]/Momentos["m00"])
            y=int(Momentos["m01"]/Momentos["m00"])
            # sacar area
            if area<11700 and area>10000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6,"P/. 500",(x,y),font,0.75,(0,255,0),2)
                suma1 = suma1+500
            if area<10800 and area>10000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6,"P/.50",(x,y),font,0.75,(0,255,0),2)
                suma2 = suma2+50
        # finalizacion       
        total = suma1 + suma2
        print("sumatoria total en pesos:",round(total,2))
        cv2.imshow("Image_A6",imagen_A6)
        cv2.imshow("camara",camara)
    if cv2.waitKey(1) == ord("s"):
        break

capturavideo.release()
cv2.destroyallwindows()


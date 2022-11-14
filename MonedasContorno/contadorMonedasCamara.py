

import cv2 as cv


# (VideoCapture) es para abrir la camara de video, se le agrega el (0) para buscar camaras que trabajen desde el pc y cuando es (1) serian camaras internas como camaras de seguridad
capturarVideo = cv.VideoCapture(1)

if not capturarVideo.isOpened():
    print("camara no encontrada")
    # (exit) para fianalizar 
    exit()
while True:
    #(read) arroja dos valores 
    _,Camara = capturarVideo.read()
    # mostras grises 
    grises = cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)
    cv.imshow("camara en contrada",grises)
    # le agrego un (1) por que es continuo, la funcion (ord) tecla para reconocer 
    if cv.waitKey(1)==ord("q"):
        break
# detener 
capturarVideo.release()
cv.destroyallwindows()
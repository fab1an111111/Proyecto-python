

# findContours
#Funcion de Opencv
# esta funcion nos ayudara a analizar contornos,los requisitos para que funciones para

#1.- umbral = umbralisada es decir una imagen blanco y negro,que este separado del objeto
#2.- mode = salida de datos 

#3.- method = metodo para encontrar contornos
# APROX_NONE, agarra todo los puntos limite y se almacenan 
# APROX_SIMPLE: elimina todos los puntos redundante y comprime el contorno, ahorrando asi memoria

cv2.findContours(umbral,mode,method)
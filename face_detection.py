import cv2 
 
#Cargamos nuestro classificador de Haar:
cascada_rostro = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#haar_cascade = cv.CascadeClassifier('haar_face.xml')
  
#Cargamos la imagen y la convertimos a grises:
img = cv2.imread('./images/imagen_input.jpg')
cv2.imshow('Output', img)
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#Buscamos los rostros:
coordenadas_rostros = cascada_rostro.detectMultiScale(img_gris, 1.3, 5)

 
 
#Ahora recorremos el array 'coordenadas_rostros' y dibujamos los rectángulos sobre la imagen original:
for (x,y,ancho, alto) in coordenadas_rostros:
    cv2.rectangle(img, (x,y), (x+ancho, y+alto), (0,0,255) , 3)
 
 
#Abrimos una ventana con el resultado:
cv2.imshow('Output', img)
print("\nMostrando resultado. Pulsa cualquier tecla para salir.\n")
cv2.waitKey(0)
cv2.destroyAllWindows()
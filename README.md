# Deteción y reconocimiento de caras

1. [Descargar el clasificador](#schema1)
2. [Cargamos la imagen y la convertimos a grises](#schema2)
3. [Buscamos los rostros](#schema3)
4. [Ahora recorremos el array 'coordenadas_rostros' y dibujamos los rectángulos sobre la imagen original](#schema4)
5. [Abrimos una ventana con el resultado](#schema5)
<hr>

<a name="schema1"></a>

# 1. Descargar el clasificador

Ir a : https://github.com/opencv/opencv/tree/master/data/haarcascades y descargar `haarcascade_frontalface_alt.xml` y guardarlo. 
~~~python
cascada_rostro = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
~~~
<hr>

<a name="schema2"></a>

# 2. Cargamos la imagen y la convertimos a grises
En este caso no tendríamos que hacer la conversión a gris porque la imagen ya está en blanco y negro, pero si usamos otra foto en color hay que convertirla a gris
~~~python
img = cv2.imread('imagen_input.jpg')
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
~~~

<hr>

<a name="schema3"></a>

# 3. Buscamos los rostros
La función `detectMultiScale()` requiere una imagen en escala de grises. Esta es la razón
por la que hemos hecho la conversión de BGR a Grayscale.  `'1.3' y '5'` son parámetros estándar para esta función.

El primero es el factor de escala `scaleFactor = 1.3`: la función intentará encontrar rostros escalando la imagen varias veces, y este factor indica en cuánto se reduce la imagen.
El segundo parámetro se llama `minNeighbours = 5` e indica la calidad de las detecciones: un valor elevado resulta en menos detecciones pero con más fiabilidad.

~~~python
coordenadas_rostros = cascada_rostro.detectMultiScale(img_gris, 1.3, 5)
~~~
<hr>

<a name="schema4"></a>

# 4. Ahora recorremos el array 'coordenadas_rostros' y dibujamos los rectángulos sobre la imagen original
~~~python

for (x,y,ancho, alto) in coordenadas_rostros:
    cv2.rectangle(img, (x,y), (x+ancho, y+alto), (0,0,255) , 3)
 
~~~

<hr>

<a name="schema5"></a>

# 5. Abrimos una ventana con el resultado
~~~python
cv2.imshow('Output', img)
print("\nMostrando resultado. Pulsa cualquier tecla para salir.\n")
cv2.waitKey(0)
cv2.destroyAllWindows()
~~~
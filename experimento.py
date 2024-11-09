# Experimento para convertir fondo claro en fondo blanco

import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('foto_clara.jpg')

# Definir el rango de colores claros a reemplazar
lower_bound = np.array([200, 200, 200])  # Limite inferior en el espacio BGR
upper_bound = np.array([255, 255, 255])  # Limite superior en el espacio BGR

# Crear una máscara para los píxeles en el rango de colores claros
mask = cv2.inRange(img, lower_bound, upper_bound)

# Cambiar los píxeles claros a blanco
img[mask != 0] = [255, 255, 255]

# Guardar o mostrar el resultado
cv2.imwrite('foto_blanca.jpg', img)
cv2.imshow('Resultado', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
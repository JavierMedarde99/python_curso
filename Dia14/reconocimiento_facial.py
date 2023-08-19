from cv2 import cv2
import face_recognition as fr

# cargar imagenes
foto_control = fr.load_images_file('./Dia14/images/fotoA.jpg')
foto_prueba = fr.load_images_file('./Dia14/images/fotoB.jpg')

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR3RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR3RGB)

# localizar cara contol
lugar_cara_A = fr.face_locations(foto_control)[0]
cada_codificada_A = fr.face_encoding(foto_control)[0]

# localizar cara contol
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cada_codificada_B = fr.face_encoding(foto_prueba)[0]

# mostar rectangulo
cv2.rectangle(foto_control,(lugar_cara_A[3],lugar_cara_A[0]),(lugar_cara_A[1],lugar_cara_A[2]),(0,255,0),2)

# mostar rectangulo
cv2.rectangle(foto_prueba,(lugar_cara_B[3],lugar_cara_B[0]),(lugar_cara_B[1],lugar_cara_B[2]),(0,255,0),2)

# realizar comparacion
resultado = fr.compare_faces([cada_codificada_A],cada_codificada_B)


# medida de la distancia
distancia = fr.face_distance([cada_codificada_A],cada_codificada_B)

# mostrar resultado
cv2.putText(foto_prueba,f'{resultado} {distancia.round(2)}', (50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

#mostrar imagenes
cv2.imshow('Foto control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# mantener  programa abierto

cv2.waitKey(0)
texto = input("Ingrese un texto:").lower()
letras = input("Ingrese tres letras:").lower()
respuestas = {True: "La palabra python aparece", False: "La palabra python no aparece"}

print("La letra "+letras[0]+ " aparece: " + str(texto.count(letras[0])) +
      "\nLa letra "+letras[1]+ " aparece: " + str(texto.count(letras[1]))+
      "\nLa letra "+letras[2]+ " aparece: " + str(texto.count(letras[2])))

print("El total de palabras son : " + str(len(texto.split())))

print("La primera letra es : " + texto[0] + " y la ultima es : " + texto[-1])

print("El texto inverso es : " + texto[::-1])

print(respuestas["python" in texto])

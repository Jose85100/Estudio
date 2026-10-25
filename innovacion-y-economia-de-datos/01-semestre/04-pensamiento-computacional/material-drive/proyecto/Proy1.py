import re
#https://www.youtube.com/watch?v=DQXm6bIZgvk&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=73
#Código para abrir documento txt
with open("datos/prub.txt","r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea)

#Busca palabra en string
Cade="Mirando fijamente en la oscuridad a alguna estrella lejana,la emoción de saber lo solos que estamos"

print(re.search("solos", Cade))#verificación de existencia de texto
if re.search("solo", Cade) is not None:
    print("si encontre el texto")
else:
    print("No he encontrado el texto")

texto= "la"
texto_encontrado=re.search(texto,Cade)
print(re.findall(texto,Cade))#DEVUELVE LAS VECES QUE SE REPITE UNA PALABRA
print(len(re.findall(texto,Cade)))#Tamaño de la lista devuelta

print(texto_encontrado.start())#devuelve el número de caracter de 0 al número donde empieza
print(texto_encontrado.end())#devuelve el número de caracter donde termina
print(texto_encontrado.span())#donde empieza y termina




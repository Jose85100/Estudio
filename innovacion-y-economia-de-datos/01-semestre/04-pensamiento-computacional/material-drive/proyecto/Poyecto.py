#PROYECTO
#RECONOCIMIENTO DE TEXTOS LEGALES
#JOSE GABRIEL OROSCO

import re
import os

tom=[]
with open("datos/CONST ART 1.txt","r", encoding="utf-8") as archivo:
    pum=archivo
    for linea in pum:
        #print(linea)
        tom.append(linea)

print("La cantidad de articulos encontrados es", len(re.findall("ARTICULO", str(tom)))+1)

for elemento in tom: #devuelve los que tengan caracter determinado
    if re.findall("ARTICULO", elemento):
        print(elemento)
    if re.findall("TITULO", elemento):
        print(elemento)
    if re.findall("PARÁGRAFO", elemento):
        print(elemento)
    if re.findall("CAPITULO", elemento):
        print(elemento)
print("Pulse 1 para buscar palabra")

r=int(input())
if r==1:
    p=input("Ingrese una palabra a buscar")
    for elemento in tom:  # devuelve los que tengan caracter determinado
        if re.findall(p, elemento, re.IGNORECASE):
            print(elemento)
else:
    None
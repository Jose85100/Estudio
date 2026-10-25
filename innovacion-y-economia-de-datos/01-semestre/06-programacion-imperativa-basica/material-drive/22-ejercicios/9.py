#Escribir un programa que calcule la longitud y el área de una circunferencia, capturando el 
#valor del radio.
import math
r=float(input("Ingrese el valor de el radio"))
pi=math.pi
long=(2*pi)*r
are=math.pi*(r*r)
print("La longitud de la circunferencia es ",long)
print("El area de la circunferencia es ",are)

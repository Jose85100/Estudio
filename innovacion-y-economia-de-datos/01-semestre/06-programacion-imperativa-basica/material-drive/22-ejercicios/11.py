#Escribir un programa que calcule el volumen de una esfera de radio = r volumen de la esfera 
#= 4/3 * PI * radio3
import math
ra=float(input("Ingresar el valor del radio"))
v_esfera=4/3*math.pi*(ra*ra*ra)
print("El volumen es", v_esfera)

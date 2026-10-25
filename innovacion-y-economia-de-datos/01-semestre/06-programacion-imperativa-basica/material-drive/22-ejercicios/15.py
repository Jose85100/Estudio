#Escribir un programa que calcule las raíces de una ecuación de 2° grado
import math
from math import sqrt

a=int(input("Ingrese el valor de a"))
b=int(input("Ingrese el valor de b"))
c=int(input("Ingrese el valor de c"))
x = (b**2)-(4*a*c)
x1 = (-b + math.sqrt(x))/(2*a)
x2 = (-b - math.sqrt(x))/(2*a)
#d=(-b+(sqrt(b**2-(4*a*c)))/(2*a))
print(x1)
print(x2)

#Escribir un programa que calcule el área de un rectángulo a partir de sus coordenadas x1, 
#y1,x2, y2
x_1=int(input("Ingrese el valor de la cordenada x"))
x_2=int(input("Ingrese el valor de la cordenada x"))
y_1=int(input("Ingrese el valor de la cordenada y"))
y_2=int(input("Ingrese el valor de la cordenada y"))
b=x_2-x_1
h=y_2-y_1
a=b*h
print("El area es:",a)


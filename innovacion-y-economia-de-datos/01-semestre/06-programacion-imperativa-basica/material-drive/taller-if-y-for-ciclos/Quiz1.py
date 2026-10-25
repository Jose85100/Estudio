#Programa para imprimir las tablas de multiplicar
#Jose Gabriel Orosco
#26/08/2021
num=int(input("Ingrese la tabla que quiere consultar"))
if num<10:
    print("Tabla del ",num)
    for f in range(0,11):
        multi=num*f
        print(num,"x",f,"=",multi)
elif num>10:
    print("Tabla del ",num)
    for f in range(0,num+1):
        multi=num*f
        print(num,"x",f,"=",multi)

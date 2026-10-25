#Programa de recibir tres números y ordenar
#Jose Gabriel Orosco
#19/08/2021
lis=[]
for i in range(3):
    r=int(input("Ingresar un número"))
    lis.append(r)
lis.sort()
print(lis)

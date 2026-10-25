#Llenar un arreglo con los 100 primeros números enteros y
#los muestre en pantalla en orden descendente
#Jose Gabriel Orosco
num=[]
for i in range(0,101):
    num.append(i)
for pasa in range(len(num)-1):
    for i in range(len(num)-1-pasa):
        if num[i]<num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
print(num)

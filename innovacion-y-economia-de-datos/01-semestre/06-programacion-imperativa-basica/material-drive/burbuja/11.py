#Llenar un arreglo con los 100 primeros números pares y muestre su suma.
#Jose Gabriel Orosco
k=[]
pp=0
for j in range(0,100,2):
    k.append(j)
for i in k:
    pp=pp+i  
print(pp)

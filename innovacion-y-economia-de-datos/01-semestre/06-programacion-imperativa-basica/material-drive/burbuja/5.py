#Llenar un arreglo con los números impares comprendidos entre
#1 y 100 y los muestre en 
#pantalla en orden ascendente.
#Jose Gabriel Orosco
num=[]
for i in range(0,100):
    l=i%2
    if l!=0:
        num.append(i)
for pasa in range(len(num)-1):
    for i in range(len(num)-1-pasa):
        if num[i]>num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
print(num)
        

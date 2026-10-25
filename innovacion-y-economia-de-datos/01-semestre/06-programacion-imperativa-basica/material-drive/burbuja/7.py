#Leer 10 números por teclado, los almacene en un arreglo y los ordene de forma 
#ascendente.
#Jose Gabriel Orosco

num=[]

for i in range(0,11):
    r=int(input("Ingrese un número"))
    num.append(r)

    
    
for pasa in range(len(num)-1):
    for i in range(len(num)-1-pasa):
        if num[i]>num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
print(num)

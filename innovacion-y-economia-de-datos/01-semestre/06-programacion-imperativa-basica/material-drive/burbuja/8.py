#Leer 10 números por teclado, 5 para un arreglo y 5 para otro arreglo distinto. Mostrar los 10 
#números en pantalla mediante un solo arreglo.

a=[]
b=[]
num=[]
#no me dejó concatenar
for i in range(0,5):
    r=int(input("Llene el arreglo 1"))
    a.append(r)
for i in range(0,5):
    t=int(input("Llene el arreglo 2"))
    b.append(t)
for i in a:
    num.append(i)
for i in b:
    num.append(i)
    
    
for pasa in range(len(num)-1):
    for i in range(len(num)-1-pasa):
        if num[i]>num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
print(num)

#Leer 5 números por teclado, los copie a otro arreglo
#multiplicados por 2 y los muestre todos 
#ordenados usando un tercer arreglo
#Jose Gabriel Orosco
op=[]
pp=[]
num=[]
for i in range(0,5):
    uj=int(input("Ingrese un número"))
    op.append(uj)
for ñ in op:
    p=ñ*2
    pp.append(p)
for o in pp:
    num.append(o)
for pasa in range(len(num)-1):
    for i in range(len(num)-1-pasa):
        if num[i]>num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
print(num)

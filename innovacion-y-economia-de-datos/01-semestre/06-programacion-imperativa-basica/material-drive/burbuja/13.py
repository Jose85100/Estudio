datos=int(input("Cuantos datos va agregar?"))
num=[]
mo=0
for i in range(0,datos):
    p=int(input("Ingrese un número"))
    num.append(p)

for pasa in range(len(num)-1):
    for i in range(len(num)-1-pasa):
        if num[i]>num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
print(num)


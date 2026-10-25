"""a=10
b=999
c=0
print("Los capicuas encontrados son los siguientes:")
for i in range(a,b+1):
    numa=str(i)
    num=list(numa)
    if num==num[::-1]:
        pal=''.join(num)
        c+=1
        print(pal)
        
print("Total de Capicuas:",c)"""
import time
inicio = time.time()
a=10
d=0
c=0
num=[]
for h in range(10,90):
    e=h
    for i in range(10,90):
        d=e*i
        y=len(str(d))
        #a+=1
        if y == 3:
            if d in num:
                a+=1
            else:
                num.append(d)
        else:
            a+=1
cs=sorted(num)
ut=[]
for i in cs:
    numa=str(i)
    num2=list(numa)
    if num2==num2[::-1]:
              cap=''.join(num2)
              ut.append(cap)
              c+=1
              print(cap)

            
#print(ut)
print("El mayor capicúa del resultado del producto de dos números con tres dígitosa, es", max(ut)) 
print("Total de Capicuas:",c)
fin = time.time()
print("tiempo de programa", fin-inicio)
print(num2)
print(cs)


 

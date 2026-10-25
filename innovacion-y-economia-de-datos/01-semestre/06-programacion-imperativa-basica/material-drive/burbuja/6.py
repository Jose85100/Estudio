me=[]
contS=0
contM=1
for i in range(10):
    num=int(input("Ingrese el número"))
    me.append(num)
for i in me:
        contS=contS+i
for i in me:
    contM=contM*i
print(me)
print(contS)
print(contM)
print(contS/len(me))


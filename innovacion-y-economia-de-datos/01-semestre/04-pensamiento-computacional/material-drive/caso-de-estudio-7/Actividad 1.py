y=[]
y2=0
for i in range(1,6):
    p=int(input("Ingrese un número"))
    y.append(p)
    y2=y2+p
print(y)
o=y2/5
print("media", o)
y.append(o)
print(y)


#Ejercicio propuesto corte 2
#número primo de la posición 999 en la lista
#Jose Gabriel Orosco
ku=0
uj=[]
n=10000

for i in range(2,n+1):
    contador=0
    for j in range(1,n+1):
     if i%j==0:
      contador+=1
    if contador==2:
     uj.append(i)
"""for i in range(0,10000):
    if i%3==0 or i%5==0:
         uj.append(i)"""
print(uj[999])
print(uj[6])


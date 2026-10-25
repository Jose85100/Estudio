#Si listamos todos los números naturales menores de 10 que son múltiplos de 3 o 5, 
#obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.
#Encontrar la suma de todos los múltiplos de 3 ó 5 menores o iguales que 999.

#Jose Gabriel Orosco
ku=0
uj=[]
for i in range(0,999):
    if i%3==0 or i%5==0:
         uj.append(i)
for i in uj:
    ku=ku+i
#print(uj)
print(ku)

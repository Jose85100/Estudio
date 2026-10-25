#Ejercicio sumar multiplos de 3 y 5
#11/Noviembre
#Jose Gabriel Orosco
sumatoria=0
for i in range(0,1000):
    if i%3==0 or i%5==0:
        sumatoria+=i
print(sumatoria)

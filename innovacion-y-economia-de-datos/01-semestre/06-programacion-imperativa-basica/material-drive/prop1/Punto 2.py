import time
inicio =time.time()
for i in range(10000):  
    #print("introduzca el numero")
    #print("Buscando")
    numero =i
    #int(input()) #aquí se lee el número entero
    contador = 0
    #print(numero)
    for divisor in range(1,20):
        if (numero % divisor) == 0 :
            #print(divisor,"es divisor")
            contador += 1
            #print(contador)
if contador==19:
    print("el numero ",numero," tiene ",contador," divisores")
    #break
fin = time.time()
print("tiempo de programa", fin-inicio)

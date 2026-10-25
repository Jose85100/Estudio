#reloj digital
#Jose Gabriel Orosco
import time
import os
seg=0
print("Configure la hora, ingrese la hora y después los minutos")
hor=int(input("Ingrese la hora"))
mint=int(input("Ingrese la los minutos"))

while seg!=60:
    for i in range(0,60):
        seg=i
        time.sleep(1)
        if seg==59:
            mint=mint+1
        
        if mint==59:
            hor=hor+1
    
        print("===============")
        print("||",hor,":",mint,":",seg,"||")
        print("===============")
        os.system('cls')
    if seg==0:
        seg=seg-59
    if mint==59:
        mint=mint-59
    if hor==24:
        hor=hor-24



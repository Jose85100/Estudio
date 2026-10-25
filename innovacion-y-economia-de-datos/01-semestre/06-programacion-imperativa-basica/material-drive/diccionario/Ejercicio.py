#Ejercicio diferencia de la suma del cuadrado de x numeros
# y el cuadrado de la suma de x números
#Jose Gabriel Orosco
#9/11
resul={}
archivo="Resultado.txt"

def cuadr(r):
    if t<1:
        y=0
        for i in range(r+1):
            o=i**2
            y+=o

    if t==1:
        e=0
        for i in range(r+1):
            e+=i
            y=e**2
    return (y)
def resultado(archivo=archivo):
    try:
        f=open(archivo,mode='r')
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        print(f.readlines())
        f.close()
    return
def añadir(kr):
    #
    try:
        f=open(archivo, mode='a')
    except FileNotFoundError:
        print("el archivo no existe")
    else:
        f.write('\n')
        f.write(kr)
        f.close()
    return

t=0
r=int(input("Ingrese la cantidad de números a evualuar"))
k1=cuadr(r)
t+=1
k2=cuadr(r)
kr=k2-k1
print(k2,k1,kr)
resul.setdefault('Resultado', kr)
añadir(str(resul))



#Punto 2 taller manejo de archivos
#Recibe 8 números por teclado aleatorios
#Los clasifica en pares e impares
#Y los agrega a un archivo .txt
#4/11
#Jose Gabriel Orosco
def ordenar(p,o):
    p2=sorted(p) #ordena de manera ascendente p
    par = []
    impar = []

    # Ordena los números en dos listas, par e impar
    if o=='par':
        for i in p2:
            if i % 2 == 0:
                par.append(i)
    elif o=='impar':
        for i in p2:
            if i%2 != 0:
                impar.append(i)
    par.sort()
    impar.sort()
    if len(par)>1:
        return par
    elif len(impar)>1:
        return impar

archivo='lista.txt'
def ventas(archivo=archivo):
    try:
        f=open(archivo,mode='r')
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        print(f.readlines())
        f.close()
    return

def añadir_lista(l):
    #
    try:
        f=open(archivo, mode='a')
    except FileNotFoundError:
        print("el archivo no existe")
    else:
        if l==par:
            f.write('Par'+'\n')
        elif l==impar:
            f.write('Impar'+'\n')

        for i in l:
            f.write((str(i))+'\n')
        f.close()
    return


p=[]
print("Ingrese 8 números")
for i in range(1,9):
    print(i, end=" ")
    l=int(input("Ingrese el número "))
    p.append(l)

par=ordenar(p,'par')
impar=ordenar(p,'impar')
print(par)
print(impar)
#par.insert(0,"par")
#impar.insert(0,"impar")
añadir_lista(par)
añadir_lista(impar)

l=int(input("Ingrese un número "))

def verf(l):
    g=0
    for i in range(1,l+1):

        y=l/i
        if l%i==0:
            g+=1
        #print(l,'/',i)
        #print (y)
        if g>2:
            break

    if g>2:
        a= ("No es primo")
        return a
    elif g==2:
        b=("Es primo")
        return b

r=verf(l)
print(r)
#Programa cálculo de ganancia a determinada tasa de interés
#Jose Gabriel Orosco
#23 de noviembre
def datos():
    d = {}
    nombre=input("Ingrese su nombre ")
    d.setdefault('nombre', nombre)
    telf=int(input("Ingrese su teléfono "))
    d.setdefault('telefono', telf)
    edad=int(input("Ingrese su edad "))
    d.setdefault('edad',edad)
    dinero_in=int(input("Ingrese el dinero a depositar "))
    d.setdefault('Dinero', dinero_in)
    tasaint=int(input("Ingrese la tasa de interés del año "))
    d.setdefault('Tasa', tasaint)
    return d
def opera(d):
    k= d.get('Dinero')
    j=d.get('Tasa')
    j2= 0

    for i in range(12):
        o=j/12
        tr2=(o*(k+j2))/100
        j2=j2+tr2
    return j2

def imprim(r,d):
    z=d.get('Dinero')
    z1=d.get('nombre')
    print(z1,",usted agregó",z,"y tuvo una gancia de:", r)

d=datos()
r=opera(d)
imprim(r,d)

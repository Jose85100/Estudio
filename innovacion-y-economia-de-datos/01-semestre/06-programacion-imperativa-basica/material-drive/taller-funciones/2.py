#Ejercicio que calcula el total de ganacia por las horas habituales y horas extras
#Jose Gabriel Orosco
#19 de octubre
t=input("Ingrese su nombre")
sul_h=int(input("Ingrese el valor de su sueldo por semana"))#son horas por semana
num_h=int(input("Ingrese el número de horas trabajadas por semana"))

def lol(a,b):
    p_hora=a/b
    if b>40:
        hor_e=b-40
        o=hor_e*(p_hora*1.75)
        tot=o+a
    elif b<40:
        tot="lo sentimos,no alcanzó el total de horas requerido"
    return(tot)
r=lol(sul_h,num_h)
print(t,"su ganacia total es:",r)

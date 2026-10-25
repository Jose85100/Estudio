#Sistema de la nómina
#Jose Gabriel
#31/08
print("===============================")
nom=input("Ingrese su nombre")
sueld=float(input("Ingrese el valor del sueldo por mes"))
horex=int(input("Ingrese las horas extras"))
pag_extra=0
ces=0
prima=0
fonds=0
print("Sueldo básico", sueld)
if horex != 0:
    valor_h=sueld/240
    rec=(35*valor_h)/100
    valor_horex=valor_h+rec
    pag_extra=horex*valor_horex
    sueld=sueld+pag_extra
    
if sueld>3900000:
    fonds=(1*sueld)/100
if sueld>0:
    salud=(4*sueld)/100
    pension=(4*sueld)/100
    vaca=(4.17*sueld)/100
if sueld<11900000:
    ces=(8.33*sueld)/100
    prima=(8.33*sueld)/100

print("||""El sueldo es: ", sueld)
print("||""Horas extra: ", pag_extra)
print("||""Deducciones:")
print("||""Aporte al fondo de solidarida: ", fonds)
print("||""El aporte a salud es: ", salud)
print("||""El aporte a pensión es: ", pension)
print("||""Prestaciones socials: ")
print("||""La nómina para las censantias: ",ces)
print("||""La prima de servicios es: ", prima)
print("||""Las vacaciones equivalen a: ", vaca)
print("||""Total a pagar:", sueld-(fonds+salud+pension))
      

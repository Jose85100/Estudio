hor1=int(input("Ingrese el valor de las horas trabajadas"))
precio_s=int(input("Ingrese el valor del suledo semanal"))
suel_hor=precio_s/40
if hor1>40:
    hor_extr=hor1-40
    valor_extr=suel_hor*hor_extr*1,75
    print("El sueldo es:", precio_s+ hor_extr)
elif hor1 <= 40:
    print("El sueldo es:",precio_s)

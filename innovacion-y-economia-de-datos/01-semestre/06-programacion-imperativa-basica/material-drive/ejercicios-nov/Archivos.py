#Programa para crear un archivo
#ARCHIVO.CSV
#fUNCION PARA AGREGAR
archivo='ventas.csv'
def ventas(archivo=archivo):
    try:
        f=open(archivo,mode='r')
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        print(f.readlines())
        f.close()
    return
def añadir_venta(id,mes,dia,hora,venta,archivo=archivo):
    #
    try:
        f=open(archivo, mode='a')
    except FileNotFoundError:
        print("el archivo no existe")
    else:
        f.write(id+','+mes+','+dia+','+hora+','+venta+'\n')
        f.close()
    return

añadir_venta('12345','08','27','12:00', '500000')
añadir_venta('23456','10','28','13:00','450000' )
añadir_venta('72345','02','29','14:00', '100000')


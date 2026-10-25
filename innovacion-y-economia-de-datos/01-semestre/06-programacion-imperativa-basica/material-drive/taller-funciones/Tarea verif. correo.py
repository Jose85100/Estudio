import re
#Programa que valida la direrrión de correo electronico
#Se verifica la exitencia de un @, las terminación en .com y .co
#y que la información dada no está vaca
#Jose Gabriel Orosco
#23/10
correo=input("Ingrese su correo electrónico")

def ver(correo):
    error=0
    texto= ".com"
    texto2= "@"
    check=0

    #verificación de correo vacio 
    if len(correo)<14:
        error+=1



    #texto_encontrado=re.search(texto, correo)
    t=[]
    #for i in (correo):
    #    t.append(i)
    #print(t)
    #print(re.findall(texto,correo))#DEVUELVE LA palabra, las veces QUE SE REPITE UNA PALABRA
    #print(len(re.findall(texto,correo)))#Tamaño de la lista devuelta, numero de veces que se devuelve

    # verificación de cantidad de .com y @
    if len(re.findall(texto2,correo))>1:
        error=error+1

    if len(re.findall(texto,correo))>1:
       error=error+1


    #print(re.search(".com", correo))#verificación de existencia de texto
    #Verificación del arroba
    if "@" in correo:
        check += 1
        #print("Primera verificación @")
    elif "@" not in correo:
        #print("No hay arrobas")
        error+=1

    if re.search("@", correo) is not None:
        check += 1
        #print("si encontre el arroba")
    else:
        #print("No he encontrado el arroba")
        error=error+1

    #Verificación de espacios
    if re.search(" ", correo) is not None:
        error=error+1
        #print("si encontre espacios")
    else:
        #print("No he encontrado espacios")
        check += 1



    #Verificación del .com
    if re.search(".com$", correo) or re.search(".co$", correo)is not None:
        #print("si encontre el texto")
        check += 1
    else:
        #print("No he encontrado el texto")
        error=error+1

    #Validación
    if error==0:
       p="Su correo electronico es correcto"
       check += 1
    elif error>0:
        p="El correo es incorrecto, verificar"
    return(p)

t=ver(correo)
print(t)

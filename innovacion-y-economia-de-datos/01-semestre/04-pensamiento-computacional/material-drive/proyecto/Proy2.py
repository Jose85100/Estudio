import re
lista_name=['Jose Orosco',
            'María Niño',
            'Daniela Muñoz',
            'Camila Payán',
            'Daniela Martinez',
            'Ana Niño',
            'Niños',
            'Niñas']
for elemento in lista_name:#todos los nombre que encuentra
    if re.findall('^Daniela', elemento):
        print(elemento)
for elemento in lista_name: #devuelve los que termina en ese texto
    if re.findall("Niño$", elemento):
        print(elemento)

for elemento in lista_name: #devuelve los que tengan caracter determinado
    if re.findall("[ñ]", elemento):
        print(elemento)

for elemento in lista_name: #deacuerdo a un patrón con os o as "camión" o "camion"
    if re.findall("niñ[oa]s", elemento):
        print(elemento)

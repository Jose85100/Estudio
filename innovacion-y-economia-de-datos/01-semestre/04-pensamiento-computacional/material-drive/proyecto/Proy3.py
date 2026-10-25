import re
lista_name=['Ma1',
            'Se1',
            'Ma2',
            'Ba1',
            'Ma3',
            'Va1',
            'Va3'
            'Ma4']

"""for elemento in lista_name: #[o-t], con un rang, entre la  y la t
    if re.findall("{^[oa]$", elemento):
        print(elemento)"""

for elemento in lista_name:rango con datos #Negació[^0-3]#Más datos Ma[0-3A-B] Ma[.:]
    if re.findall("Ma[0-3]", elemento):
        print(elemento)
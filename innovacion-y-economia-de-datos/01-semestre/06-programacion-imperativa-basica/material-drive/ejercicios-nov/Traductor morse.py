diccmor = {"A": ".-","B": "-...","C": "-.-.","CH": "----","D": "-..",
    "E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..",
    "M": "--","N": "-.","Ñ": "--.--","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-",
    "V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","0": "-----","1": ".----","2": "..---",
    "3": "...--","4": "....-","5": ".....","6": "-....","7": "--...", "8": "---..","9": "----.",
    ".": ".-.-.-", ",": "--..--",":": "---...", "?": "..--..", "'": ".----.","-": "-....-",
    "/": "-..-.", "\"": ".-..-.","@": ".--.-.","=": "-...-", "!": "−.−.−−",
}
print("Elija una opción")
print('1.Español to morse')
print('2.Morse a español')
op=int(input())
def morse(a):
    a=a.upper()
    p=[]
    for i in a:
        if i in diccmor:
            o=diccmor.get(i)
            p.append(o)
    return p

"""def letra(a):
    a=a.upper()
    e=[]
    for i in a:"""

if op==1:
    frase1=input('Ingrese la frase a traducir')
    r=morse(frase1)
    print(r)
elif op==2:
    frase2=input('Ingrese la frase a traducir')
    t=letra(frase2)
else:
    print('Opción no valida')
op=int(input())

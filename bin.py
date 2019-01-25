def decode(msg) :#passer du binaire au texte
    tabl = msg.split()
    i=0
    txt=""
    while i < len(tabl) :
        c=chr(int(tabl[i], 2))
        txt+=c
        i+=1
    return txt

def code(msg) :#passe du texte au binaire
    txt=""
    for char in msg :
        c=bin(ord(char))
        txt=txt+' '+c
    return txt

print("Convertisseur binaire \nBy ton ninchat.\n")
choix=""
while choix != 'exit' and (choix == "" or choix == '1' or choix == '2'):
    print("\nTexte vers Binaire -> 1\nBinaire vers Texte -> 2\nexit -> sorir")
    choix = input("\:>")
    if choix == '1' :
        print("\n",code(input("Texte :\n/>")))
    elif choix == '2' :
        print("\n",decode(input("Binaire :\n/>")))
    else :
        print("[*]Exiting\n")

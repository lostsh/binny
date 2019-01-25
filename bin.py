def decode(msg) :#function get a binary number and output a  text or letter
    tabl = msg.split()
    i=0
    txt=""
    while i < len(tabl) :
        c=chr(int(tabl[i], 2))
        txt+=c
        i+=1
    return txt

def code(msg) :#input the text and output the binary text
    txt=""
    for char in msg :
        c=bin(ord(char))
        txt=txt+' '+c
    return txt

print("Binary converter \nBy shutdown_01011\n")
choix=""
while choix != 'exit' and (choix == "" or choix == '1' or choix == '2'):
    print("\nText to Binary -> 1\nBinary to Text -> 2\nexit ->to exit")#if you exit ... this must creat a unicorn
    choix = input("\:>")
    if choix == '1' :
        print("\n",code(input("Texte :\n/>")))
    elif choix == '2' :
        print("\n",decode(input("Binaire :\n/>")))
    else :
        print("[*]Exiting\n")

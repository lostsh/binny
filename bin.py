#get a bin String, and return text String
def decode(msg):
    text=""
    for letter in msg.split():
        text+=chr(int(letter, 2))
    return text

#get a String text and return a String bin
def code(msg) :
    txt=""
    for char in msg :
        c=bin(ord(char))
        txt+=' '+c
    return txt
#prompt something and return the inputed text
def prompt(msg):
    return input("%s\>"%(msg))

choix=""
while choix != 'exit' and (choix == "" or choix == '1' or choix == '2'):
    print("\nText to Binary -> 1\nBinary to Text -> 2\nexit ->to exit")
    choix = prompt("")
    try:
        if choix == '1' :
            print("\n",code(prompt("Text ")))
        elif choix == '2' :
            print("\n",decode(prompt("Binary ")))
        else :
            print("[*]Exiting\n")
    except ValueError :
        print("[!] Incorect input")
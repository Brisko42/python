def motpluslong(texte):  
    mots = texte.split()
    mot = max(mots, key=len)
    return mot


string = "1 22 333 4444 55555 666666 7777777 88888888 999999999"



motlepluslong=motpluslong(string)
print(f"renvoie du mot le plus long de la chaine de caracteres")
print(f"le mot le plus long est de : {motlepluslong}")
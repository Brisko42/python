
def reverse(string):
    
    reversed_string = string[::-1]
    return reversed_string

string = "bonjour"
print(f"message inverse")
print(f"texte original : {string}")
print(f"texte inversé : {reverse(string)}")

liste = ['1','2','3','4','5','6']
print(f"liste  inverse{reverse(liste)}")
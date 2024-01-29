
def reverse(string):
    
    reversed_string = string[::-1]
    return reversed_string

string = "bonjour"
print(f"message inverse")
print(f"texte original : {string}")
print(f"texte inversé : {reverse(string)}")
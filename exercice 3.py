def reverse(string):  
      
    reversed_string = string[::-1]
    return reversed_string

string = "il est tseli"
print(f"message inverse : {reverse(string).replace(" ", "")}")
print(f"texte original : {string.replace(" ", "")}")

if reverse(string).replace(" ", "")==string.replace(" ", ""):
    print(f"c'est un palindrome")
else:
    print(f"ce n'est pas un palindrome")



ma_liste=[1,2,3,4,5,6,7,8,9]
ma_liste2 =[7,8,9,10,11,12,4,13,14,15 ]
resultat=[]
bool=False
for element in ma_liste:
    for element2 in ma_liste2:
        if element==element2:
            resultat.append(element)
            print(f"{element}")

            bool = True
        else:
            bool = False
print(f"{resultat}")

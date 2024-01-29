import re


def datedanstexte(chaine):
    pattern = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')
    dates_trouvees = re.findall(pattern, chaine)

    return dates_trouvees


texte="les dates 12/05/2022 sont 31/01/2020 importantes 17/08/2014 moi nes "
date=datedanstexte(texte)
print(f"{date}")
"""
Créer un script qui liste tous les fichiers d'un répertoire spécifié, en incluant
leur taille. La fonction doit prendre en paramètre le dossier
"""
import os

def lister_fichiers_et_tailles(dossier):
    try:
        # Vérifie si le dossier existe
        if os.path.exists(dossier):
            print(f"Liste des fichiers dans le dossier '{dossier}':")
            
            # Liste tous les fichiers dans le dossier
            for nom_fichier in os.listdir(dossier):
                chemin_complet = os.path.join(dossier, nom_fichier)
                
                # Vérifie si l'élément est un fichier
                if os.path.isfile(chemin_complet):
                    # Obtient la taille du fichier en octets
                    taille = os.path.getsize(chemin_complet)
                    print(f"{nom_fichier} - {taille} octets")
        else:
            print(f"Le dossier '{dossier}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Spécifiez le chemin du dossier que vous souhaitez lister
dossier_specifie = r'C:\Users\itaka\Documents\Python\jour 2'
    
# Appel de la fonction avec le dossier spécifié
lister_fichiers_et_tailles(dossier_specifie)
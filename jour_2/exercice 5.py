"""
Écrire un script qui vérifie l'espace disque disponible et utilisé sur le disque
principal.
"""

import psutil

def check_disk_space():
    # Obtenez les statistiques d'utilisation du disque principal
    disk_usage = psutil.disk_usage('/')

    # Affichez les informations sur l'espace disque
    print(f"Total: {disk_usage.total / (1024 ** 3):.2f} Go")
    print(f"Utilisé: {disk_usage.used / (1024 ** 3):.2f} Go")
    print(f"Disponible: {disk_usage.free / (1024 ** 3):.2f} Go")
    print(f"Pourcentage d'utilisation: {disk_usage.percent}%")

check_disk_space()

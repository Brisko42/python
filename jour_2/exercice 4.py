"""
Créer un script qui surveille et affiche l'utilisation du CPU en pourcentage
toutes les 5 secondes.
"""


import psutil
import time

def monitor_cpu_usage():
    while True:
        # Obtenez l'utilisation actuelle du CPU en pourcentage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Affichez l'utilisation du CPU
        print(f"Utilisation du CPU: {cpu_usage}%")

        # Attendez 5 secondes avant la prochaine mesure
        time.sleep(5)

monitor_cpu_usage()
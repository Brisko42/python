"""
Écrire un script qui affiche l'utilisation de la mémoire du système.
"""
import psutil

print(f" cpu_stat :  ",psutil.cpu_stats())
print(f"cpu_percent : ",psutil.cpu_percent())
print(f" cpu_freq : ",psutil.cpu_freq())
print(f"cpu_count : ",psutil.cpu_count())
print(f"cpu_time : ",psutil.cpu_times())
print(f"process :  ",psutil.process_iter())

"""
Sorteio de 6 numeros de 1 a 60
"""

import random

print("Mega Sena!!\nSeis(6) numeroa serao sorteados no intervalo de 1 a 60.\n")

for i in range(1, 6+1, 1):
    mega_sena = random.randint(1, 60)

    print(mega_sena)
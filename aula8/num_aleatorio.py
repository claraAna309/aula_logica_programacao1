"""
Numeros aleatorios
"""

import random

print("Serão 5 numeros sorteados.")

for i in range(1, 11, 1):
    num_sorteado = random.randint(-3, 3)

    print(num_sorteado)


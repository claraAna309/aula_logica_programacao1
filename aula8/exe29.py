"""
Escreva todas as combinaçoes possiveis de dois dados
"""
ct=0

print("Dado 1 - Dado 2")
for i in range(1, 7, 1):# dado 1
    for e in range(1, 7, 1):# dado 2
        print(f"{i} - {e}")
        print("----")
        ct=ct+1
print("Quantidade de combinações: ", ct)
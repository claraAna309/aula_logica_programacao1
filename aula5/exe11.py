"""
Encontre o menor valor  de um conjunto de valores inteiros
digitados pelo usuario. Condição de saida é 0.
"""

#menor = 999999999999
menor = float('inf') # Armazena o maior valor possivel no python
ct = 0
soma = 0
media = 0

print("Digite [0] para sair do programa.\n")

while True:
    num=int(input("Digite um valor: "))

    if num==0:
        break
    if num<menor:
        menor=num
    soma=soma+num
    ct=ct+1
    media=soma/ct

print(f"\nQuantidade de numeros digitados: {ct}\n"
      f"Media dos valores digitados: {media}\n"
      f"Soma dos valores digitados: {soma}\n"
      f"Menor valor digitado: {menor}")

"""
Encontre o menor valor e o maior valor inteiro digitado oelo usuario.
Condição de saida == 0.
"""

menor = float('inf') # maior valor possivel
maior = float('-inf') #menor valor possivel
ct = 0
soma = 0
media = 0

print("Digite [0] para sair.\n")

while True:
    num=int(input("Digite um valor: "))
    if num==0:
        break

    if num<menor:
        menor=num

    if num>maior:
        maior=num

    ct=ct+1
    soma=soma+num
    media=soma/ct

if ct>0:
    print(f"\nQuantidade de numeros digitados: {ct}\n"
          f"Media dos valores digitados: {media}\n"
          f"Soma dos numeros digitados: {soma}\n"
          f"Maior valor digitado: {maior}\n"
          f"Menor valor digitado: {menor}")
else:
    print("Não foi digitado nenhum numero.")

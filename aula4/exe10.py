"""
Calculo da media aritmetica dos numeros pares
Os usuarios cai digitar varios(while) valores de entrada que pode ser par ou impar
a condição de saida sera o numero 0
"""

ct = 0
ctp = 0
soma = 0
media = 0

while True:
    num = int(input("Digite um numero, par ou impar: "))
    if num == 0:
        break
    ct = ct+1

    if num%2 == 0:
        ctp = ctp+1
        soma = soma+num
        media = soma/ctp

print(f"Quantidade de numeros digitados = {ct}"
      f"\nQuantidade de numeros pares digitados = {ctp}"
      f"\nMedia de todos os numeros pares digitados = {media}")

"""    if num == 0:
        break

if num%2==0:
    soma = soma+num
    ct = ct+1

    media = soma/ct

print(f"A quantidade de numeros pares digitados = {ct}"
      f"\nA media dos valores pares ={media}")"""
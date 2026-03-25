"""
O programa le a altura e o genero(m ou f) de varias pessoas
informar:
maior altura do grupo,
menor altura do grupo,
quant homens,
quant mulheres
"""

maior = float('-inf')
menor = float('inf')
fem = 0
mas = 0

print("Escreva 0 para sair.\n")

while True:
    alt=float(input("Digite a altura da pessoa: "))
    gen=str(input("Digite:\n[f] se for feminino\n[m] se for masculino\n"))

    # if gen!="f" and gen!="m":
    #    print("Na area do genero digite somente [f] ou [m].")
    if alt==0:
        break
    if alt<menor:
        menor=alt
    if alt>maior:
        maior=alt
    if gen=="f":
        fem=fem+1
    elif gen=="m":
        mas=mas+1
    else:
        print("Na area do genero digite somente [f] ou [m]")

print(f"Maior altura: {maior}\n"
      f"Menor altura: {menor}\n"
      f"Mulheres: {fem}"
      f"Homens: {mas}")
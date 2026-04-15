"""
Contagem de boi
usando while
"""
ct=0
ctm=0
soma=0
#media=0

print("Para sair: 0")
while True:
    num=float(input("Peso: "))
    if num==0:
        break
    ct=ct+1
    soma=soma+num
    if num>600:
        ctm=ctm+1

print(f"Quant. de bois: {ct}\n"
      f"Quant. de bois com mais de 600kg: {ctm}\n"
      f"Soma do peso: {soma}\n"
      f"Media de peso: {soma/ct}")
"""
Tabuada de multiplacação de qualque numero digitado pelo usuario
"""

num=int(input("Digite o numero da tabuada: "))
op=int(input("Qual sera a tabuada: \n1 = soma\n2 = multiplicacao\n"))

if op == 2:# MULTIPLICACAO
    print(f"Operação escolhida: Multiplicacao\nValor escolhido: {num}\n")
    for i in range(1, 11, 1):
        print(f"{num} x {i:2} = {(num*i):3}")

elif op == 1:# SOMA
    print(f"Operação escolhida: Soma\nValor escolhido: {num}\n")
    for i in range(1, 11, 1):
        print(f"{num} + {i:2} = {(num+i):2}")

else:# ERRO
    print(f"Valor digitado para operacao invalido.\nDigite somente 1(um) ou 2(dois)!!!!!!!!!!!!!")
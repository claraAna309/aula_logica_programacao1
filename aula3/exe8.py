"""
Simulação de uma calculadora de soma ou subtação
"""

operacao = int(input("\n1 - soma\n2 - subtrair\nDigite= "))
val1 = float(input("Digite o valor 1: "))
val2 = float(input("Digite o valor 2: "))

if operacao==1:
    print(f"{val1}+{val2}={val1+val2}")
elif operacao==2:
    print(f"{val1}-{val2}={val1-val2}")
else:
    print(f"Valor de operação invalido, digite outro valor.")

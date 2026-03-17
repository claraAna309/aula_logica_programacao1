"""
while == laço de repeticao
vou escrever varios numeros e para parar a repetição digita -1
"""

ct = 0# sera o contador de digitos digitados, o valor inicial dele é 0
soma = 0

print("Digite quantos numeros desejar.\nPara sair da repetição digite '-1'")

while True:
    num = int(input("Digite um numero: "))
    if num == -1:
        break# Sai da estrutura de repetição(while)
    ct = ct+1# a cada numero digitado ele soma +1 para o seu valor
    soma = soma+num

print(f"A quantidade de numeros digitados: {ct}\nA soma dos valores digitados é= {soma}")


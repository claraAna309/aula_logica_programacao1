"""
gere a sequencia de numeros int na ordem crescente
onde o usuario fornece o valor inicial e o valor final
"""
ini=int(input("Digite o valor inicial da sequancia: "))
fim=int(input("Digite o valor final da sequancia: "))
ct=0
soma=0

if ini<fim:
    for num in range(ini,fim+1,1):
        print(num)
        ct=ct+1
        soma=soma+num
else:
    for num in range(ini,fim-1,-1):
        print(num)
        ct = ct + 1
        soma = soma + num

print(f"Quant. numeros gerados: {ct}\nSoma: {soma}")

"""
Exercicio 1: Elabore um programa que calcule a soma e a subtraçãp de dois valores inteiros que serão fornecidos pelo usuario
"""

val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))

# Soma
soma = val1+val2
print("A soma dos valores é= ", soma,"\n")

# Subtração
sub = val1-val2
print("A subtração dos valores é= ", sub)

#Multiplicação
mult = val1*val2
print("A multiplicação dos valores é= ", mult)

# Acrescimo de um terceiro valor
val3 = int(input("Digite um terceiro valor: "))

soma= val1+val2+val3
print("A soma dos tres valores é= ", soma)
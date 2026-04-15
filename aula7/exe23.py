"""
Idade dos alunos
usando For
"""
ct=0
nota=0
somanot=0
idmeno=float('inf')
idmaio=float('-inf')
idade=0
somaid=0

for num in range(1,6,1):
    nota=int(input("Digite a nota: "))
    idade=int(input("Digite idade: "))
    if idade<idmeno:
        idmeno=idade
    elif idade>idmaio:
        idmaio=idade
    ct=ct+1
    somanot=somanot+nota
    somaid=somaid+idade

print(f"\nSoma idade: {somaid}"
      f"\nMedia idade: {somaid/ct}"
      f"\nAluno mais novo: {idmeno}"
      f"\nAluno mais velho: {idmaio}"
      f"\nSoma das notas: {somanot}"
      f"\nMedia das notas: {somanot/ct}")
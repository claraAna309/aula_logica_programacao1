"""
Calcular a media de uma turma que cada alino fez uma av,
não se sabe a quanrt de alunos, por isso use -1 como condição de saida.
Na saida mostre a média aritmetica da turma e a quant de alunos.
"""

ct = 0
soma = 0
media = 0
turma = str(input("Nome da disciplina: "))

print("Para sair da repetição digite '-1'")

while True:
    num = float(input("Digite a nota do aluno: "))
    if num == -1:
        break
    ct = ct+1
    soma = soma+num
    media = soma/ct

print(f"Para a quantidade de alunos = {ct} Da turma {turma}"
      f"\nA soma das notas é = {soma}\nA media é = {media:.2f}")
"""
Programa que calcula a media aritmetica de uma turma com 50 alunos.
Onde cada aluno fez um prova. O usuario vai digitar a nota dos alunos.
obs.: fazer somente com 5 notas
"""

ct=0
ctA=0# contador de aprovados
nota=0
soma=0

for num in range(1,6,1):
    nota=int(input("Digite a nota: "))
    ct=ct+1
    soma=soma+nota
    if nota>=5:
        ctA=ctA+1

print(f"\nMedia das cinco provas= {soma/ct}\nSomente {ctA} alunos foram aprovados")
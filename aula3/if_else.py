"""
if...else
se...senão

Operador relacional
== igual
!= diferente
> Maior
< Menor
>= Maior ou igual
<= Menor ou igual
"""

val1 = int(input("Digite sua idade: "))

if val1<18:
    print(f"Você é menor de idade, faltam {18-val1} anos para você ser maior de idade.")
else:
    print("Você é maior de idade")
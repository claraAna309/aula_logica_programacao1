"""
Calcular a area do triangulo, o usuario informara os dados para o calculo(valor da base e altura)
.3f = denomina quantas casas decimais serão mostradas
"""

base= float(input("Digite o valor da base do triangulo: "))
altura= float(input("Digite o valor da altura do triangulo: "))

area= (base*altura)/2

print(f"\nO valor da area do triangulo de \nbase={base} e altura={altura} é= {area:.3f}")
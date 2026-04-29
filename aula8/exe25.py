"""
Programa que impreme a tabuada de multiplacacao do numero 5, de 1 ate 10
"""

print("Tabuada do cinco(5):\n")

"""for i in range(1, 11, 1):
    mult=5*i
    print(i," x 5 = ",mult)"""

#calculo feito de forma mais curta e com o resultado saindo alinhado
for i in range(1, 11, 1):
    print(f"{i:2} x 5 = {i * 5:2}")

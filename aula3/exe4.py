"""
Converção de graus Fahrenheint(F) para Celsius(C)
"""

f = float(input("Escreva um valor em Fahrenheint: "))

convercao = 5*(f-32)/9

#print(f"A converção de {f}F para Celsius é= {convercao}")
#print(f"A converção de {f}F para Celsius é= {convercao:.2f}")
print(f"Valor em Fahrenheint: {f:.2f}\nValor em Celsius: {convercao:.3f}")
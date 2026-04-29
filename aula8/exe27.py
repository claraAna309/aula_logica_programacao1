"""
Calculadora miltiplicacao de 1 a 10.
Para cada numero fornecido sera gerada outra tabuada
"""

print("Digite 0 para sair.\n")

while True:
    num=int(input("\nTABUADA DO: "))
    if num==0:
        print("\n- - - - - - - - - - Fim do programa - - - - - - - - - -")
        break
    for i in range(1,11,1):
        print(f"{i:2} x {num} = {num*i:3}")
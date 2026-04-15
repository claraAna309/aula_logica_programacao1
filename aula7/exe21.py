"""
Calculadora que soma e subtrai
"""
op=int(input("1- soma\n2- subtração\nDigite: "))
num1=float(input("\nPrimeiro numero: "))
num2= float(input("Segundo numero: "))

if op==1:
    print(f"\n{num1} + {num2}= {num1+num2}")
elif op==2:
    print(f"\n{num1} - {num2}= {num1-num2}")
else:
    print('\033[31m' + 'Operação errada!!' + '\033[0m')
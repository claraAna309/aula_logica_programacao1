"""
Variavel= valor guardado na memoria;
Print= mostrar algo na tela.
Ver o documento PEP8
"""

print("Exemplo 1: mostrando valores")
valor1= 10 # Memória

print(valor1) # Tela

valor2= 20

print("Valor 2: ",valor2)

#------------------------------------------------------------

print("\n---------------------------------\n")

print("Exemplo 2: Comando de Soma")
x = 10 +4

print("Valor 1: ", x)

y = 2 * x

print("Valor 2: 2 x", x, "= ", y)

#------------------------------------------------------------

print("\n---------------------------------\n")

print("Exemplo 3: Mutação do valor de uma variavel")

x = 1			# Memória
print("Valo de X= ",x)		# Tela
# depois desse comando, x vale 1

x = x+1
print("Valor de X+1= ",x)
# depois desse comando, x vale 2

x = x+10
print("Valor de X+10= ",x)
# depois desse comando, x vale 12

#------------------------------------------------------------

print("\n---------------------------------\n")

print("Exemplo 4: Mostranto o valor da variavel")
print("Uso do comando 'type'\n")

valor1= 10 # Memória

print("O valor: ", valor1, "É do tipo: ", type(valor1)) # Tela

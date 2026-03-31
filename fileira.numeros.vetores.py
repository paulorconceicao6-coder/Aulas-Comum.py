import os

os.system ("cls || clear")

vetor = []

for i in range (3):
    numero = int(input("Escreva um Número: "))
    if numero < 0:
        vetor.append (0)
    else:
        vetor.append (numero)

        print ("Os Valores de Vetor são:", vetor)

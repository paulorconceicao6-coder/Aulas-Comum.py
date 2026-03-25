import os
os.system ("cls || clear")

# Criando um Vetor. 

vetor_notas = []

# Adicionando 3 Notas.
 
for i in range (3):
    nota = float(input("Digite uma nota: "))
    vetor_notas.append (nota) # Serve para por a Primeira Nota Digitada em Primeiro Lugar = 0

# Exibindo as Notas Informadas.

for i in range (3):
    print (f"Nota: {vetor_notas[i]}")
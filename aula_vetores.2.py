import os
os.system ("cls || clear")

# Criando um Vetor. 

vetor_notas = []
quantidade_notas = 3

print ("Adicionando 3 Notas.")
 
for i in range (quantidade_notas):
    nota = float(input(f"Digite a {i + 1}ª Nota: "))
    vetor_notas.append (nota) # Serve para por a Primeira Nota Digitada em Primeiro Lugar = 0

# Exibindo as Notas Informadas.

print ("\n- Exibindo As Notas Informadas. ")
for uma_nota in vetor_notas:
    print (f"Nota: {uma_nota}")
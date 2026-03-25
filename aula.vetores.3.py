import os

os.system ("cls || clear")

# Criando um Vetor. 

vetor_notas = []
quantidade_notas = 3

print (f"Adicionando {quantidade_notas} Notas.")
 
for i in range (quantidade_notas):
    nota = float(input(f"Digite a {i + 1}ª Nota: "))
    # Adicionar Nota ao Vetor.
    vetor_notas.append (nota) # Serve para por a Primeira Nota Digitada em Primeiro Lugar = 0

# sum (vetor) = soma todos os valores do setor.
media = sum (vetor_notas) / quantidade_notas

print ("- Exibindo as Notas Informadas. -")

# For Each = Percorre o vetor sem informar a quantidade.
# enumerate = através da variavel i, numera a quantidade de repetições.


print ("\n- Exibindo As Notas Informadas. ")

for i, uma_nota in enumerate (vetor_notas, start1=):
    print (f"{i}º nota: {uma_nota}")

print (f"Média: {media}")
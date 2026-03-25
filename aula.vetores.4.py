import os

os.system ("cls || clear")

vetor_num = []
quantidade_num = 5

print ("- Adicionando 5 Notas. -")

for i in range (quantidade_num):
    numero = float(input(f"Digite a {i + 1}ª Nota: "))
    vetor_num.append (numero) # Serve para por a Primeira Nota Digitada em Primeiro Lugar = 0

# Exibindo as Notas Informadas.

print ("\n- Exibindo As Notas Informadas. ")

maior_num = max (numero)
menor_num = min (numero)

print (f" A Maior Nota: {maior_num:.3f}")
print (f"A Menor Nota: {menor_num:.3f}")
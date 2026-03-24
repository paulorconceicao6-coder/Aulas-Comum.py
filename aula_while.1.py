# Exercício:

# Escreva um algoritmo que pergunte ao usuário se deseja inserir
# mais uma nota, 

# se a resposta do usuário for “N”, 

# o programa fará a média aritmética das notas informadas 

# e mostrará a média aritmética para o usuário.


# Obs.: Use um contador dentro do laço de repetição para contar a
# quantidade de iterações (loops).

import os
os.system ("cls || clear")

soma = 0.0
contador = 0
resposta = "S"

# O laço executa enquanto a resposta não for "N"
while resposta.upper() != "N":
    # Recebe a nota e a transforma em número decimal (float)
    nota = float(input("Digite a nota: "))
    
    soma += nota
    contador += 1
    
    # Atualiza a resposta para saber se o laço deve continuar
    resposta = input("Deseja inserir mais uma nota? (S/N): ")

# Verifica se o contador é maior que zero para evitar divisão por zero
if contador > 0:
    media = soma / contador
    print(f"\nA média aritmética das {contador} notas informadas é: {media:.2f}")
else:
    print("\nNenhuma nota foi inserida.")
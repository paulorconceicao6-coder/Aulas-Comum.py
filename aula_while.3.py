# Exercício:

# Faça um algoritmo que leia uma quantidade não determinada de números inteiros positivos. Calcule:

# quantidade de números pares e ímpares;

# média de valores pares

# média geral dos números lidos.

# O número que encerrará a leitura será o número zero.

# Inicialização das variáveis
qtd_pares = 0
qtd_impares = 0
qtd_geral = 0
soma_pares = 0
soma_geral = 0

valor = int(input("Digite um número inteiro positivo (0 para encerrar): "))

while valor != 0:
    if valor > 0: # Garante que só processaremos números positivos
        soma_geral += valor
        qtd_geral += 1
        
        # Se o resto da divisão por 2 for zero, é par
        if valor % 2 == 0:
            qtd_pares += 1
            soma_pares += valor
        else: # Se não é par, obrigatoriamente é ímpar
            qtd_impares += 1
    else:
        print("Por favor, digite apenas números positivos.")
        
    valor = int(input("\nDigite outro número (0 para encerrar): "))

print("\n--- RESULTADOS ---")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")

# Média dos pares
if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f"Média dos valores pares: {media_pares:.2f}")
else:
    print("Média dos valores pares: Nenhum número par foi digitado.")

# Média geral
if qtd_geral > 0:
    media_geral = soma_geral / qtd_geral
    print(f"Média geral dos números lidos: {media_geral:.2f}")
else:
    print("Média geral: Nenhum número válido foi digitado.")
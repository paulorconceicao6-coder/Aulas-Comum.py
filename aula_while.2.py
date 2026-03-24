import os
os.system ("cls || clear")

# - Construa um algoritmo que calcule a média aritmética de
# vários valores inteiros positivos, inseridos pelo usuário. 
# O final da leitura acontecerá quando for lido um valor
# negativo. 
## Mostre a média aritmética dos números informados pelo
# usuário.


soma = 0
contador = 0

# Leitura inicial antes de testar a condição do while
valor = int(input("Digite um valor inteiro positivo (negativo para parar): "))

while valor >= 0:
    soma += valor
    contador += 1
    
    # Nova leitura para decidir se o loop continua ou para
    valor = int(input("Digite outro valor (negativo para parar): "))

# Prevenção contra divisão por zero
if contador > 0:
    media = soma / contador
    print(f"\nA média aritmética dos {contador} valores informados é: {media:.2f}")
else:
    print("\nNenhum valor positivo foi inserido para calcular a média.")


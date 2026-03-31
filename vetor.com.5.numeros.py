import os
os.system ("cls || clear")
# Crie um algoritmo que preencha um vetor com 5 números, mostre a quantidade de números negativos e a soma dos números positivos desse vetor.
vetor = []

for i in range (5):
    numero = float(input("Escreva um Número: "))
    vetor.append(numero)

    negativos = 0
    soma_positivos = 0
    for numero in vetor:
        if numero <0:
            negativos += 1
        elif numero >0:
            soma_positivos += numero
            print ("\nA Quantidade de Numeros Negativos", negativos )
        print ("\nA Soma dos Números Positivos", soma_positivos)
        print ("\nFim de Programa.")

                                                                                                                                    
        print ("\nA Quantidade de Numeros Negativos", negativos )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        print ("\nA Soma dos Números Positivos", soma_positivos)
        print ("\nFim de Programa.")
0

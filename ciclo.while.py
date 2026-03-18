import os
import time 

os.system ("cls || clear")

soma = 0
QUANTIDADE_NOTAS = 3 # Quantidade de Notas que vão ser utilizadas.

for i in range (QUANTIDADE_NOTAS): # Quantidades de Notas a serem digitas.
        while True: # Laço de Repetição para validar as Notas 
             nota = float(input("\nDigite uma Nota: "))
# if nota >= 0 and nota <= 10:
#    soma += nota
# break
# else:
# print ("Nota Inválida.")
# print ("Tente Novamente.")
             if nota >= 0 and nota <= 10:
                     soma += nota
                     break
             else:
                   print ("Nota Inválida.")
                   print ("Tente Novamente. ")
       

                   
       
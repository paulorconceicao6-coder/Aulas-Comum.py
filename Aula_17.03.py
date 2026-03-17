import os
import time
os.system ("cls \\ clear")

soma = 0 
QUANTIDADE_NOTAS = 3

for i in range (4):
    nota = float (input ("Digite a nota: "))
    soma += nota
media = soma / QUANTIDADE_NOTAS
print ("A média é: ", media)
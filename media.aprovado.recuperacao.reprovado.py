import os
os.system ("cls \\ clear")

soma = 0
quantidade_notas = 3
for i in range (quantidade_notas):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota >= 0 and nota <= 10:
            soma += nota
            break
        else:
            print ("Nota Inválida. ")
            print ("Tente Novamente...\n")

media = soma / quantidade_notas

if media >= 7:
    print ("Aprovado.")
elif media >= 5:
    print ("Recuperação.")
else:
    print ("\nAluno Reprovado.")
print ("Programa Encerrado.")
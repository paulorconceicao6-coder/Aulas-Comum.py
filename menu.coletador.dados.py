
import os
os.system ("cls || clear")
print ("Bem Vindo ao programa de pesquisa de dados")

salarios = [] # Serve para a pessoa Determinar o Valor do Seu Salário.
filhos = []

while True:
    print ("\nMenu:")
    print ("1 - Adicionar Familia.")
    print ("2 - Sair e Exibir o Resultado.")

    opcao = input("Digite o Código da Opção Desejada. ")

    if opcao == "1":
     os.system ("cls || clear")  
     salario = float(input("Digite seu Salário. "))
     numero_filhos = int(input("Digite o número de Filhos. "))      
     
     salario.append (salario)
     filhos.append (numero_filhos)
     
    elif opcao == "2":
       break
    else:
       print ("Opção inválida. Por Favor, digite 1 ou 2.")

       if len(salario) > 0:
          total_familias = len(salarios)
          media_salario = sum(salarios) / total_familias
          media_filhos = sum(filhos) / total_familias
          maior_salario = max(salarios)
          menor_salario = min(salarios)

          print (f"Total de Famílias que responderam a pesquisa: {total_familias:.2f}")
          print (f"Média do Salário da População: R$ {media_salario:.2f}")
          print (f"Média do Número de Filhos: {media_filhos:.2f}")
          print (f"Maior Salário: R$ {maior_salario:.2f}")
          print (f"Menor Salário: R$ {menor_salario:.2f}")

       else:
          print ("Nenhuma Família Cadastrada.")
          
          print ("\nPrograma Encerrado. ")

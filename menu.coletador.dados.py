# Foi feita uma pesquisa entre os habitantes de uma região.  Foram coletados os dados de idade, sexo (M/F) e salário. 

# Faça um algoritmo que informe:  


# a) a média de salário do grupo;

# b) maior e menor idade do grupo;

# c) quantidade de mulheres com salário a partir de R$ 5.000,00.


# Crie um menu com três opções.


# Código |   Descrição

#        1        |   Adicionar pessoa

#        2       |   Exibir resultados

#        3       |   Sair


# O final da leitura de dados se dará com quando o usuário digitar o número código 3. 

# Ao adicionar uma pessoa, deve-se limpar o terminal e apresentar o menu novamente.


# Inicialização das variáveis

import os

def limpar_tela():
    # Verifica o sistema operacional para limpar o terminal corretamente
    # 'nt' é Windows, 'posix' é Linux/MacOS
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Variáveis para armazenar os dados
    salarios = []
    idades = []
    mulheres_5000 = 0
    
    while True:
        print("\n--- MENU DE PESQUISA ---")
        print("1 | Adicionar pessoa")
        print("2 | Exibir resultados")
        print("3 | Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            limpar_tela()
            print("--- Cadastrar Pessoa ---")
            
            # Coleta de dados
            try:
                idade = int(input("Idade: "))
                sexo = input("Sexo (M/F): ").upper()
                salario = float(input("Salário: R$ "))
                
                # Armazenar dados para cálculos
                idades.append(idade)
                salarios.append(salario)
                
                # Regra c: quantidade de mulheres com salário a partir de R$ 5.000,00
                if sexo == 'F' and salario >= 5000.00:
                    mulheres_5000 += 1
                
                print("\nPessoa adicionada com sucesso!")
                input("Pressione Enter para continuar...")
                limpar_tela()
                
            except ValueError:
                print("Erro: Entrada inválida. Tente novamente.")
                
        elif opcao == '2':
            if not salarios:
                print("\nNenhum dado cadastrado.")
            else:
                # Cálculos finais
                media_salario = sum(salarios) / len(salarios)
                maior_idade = max(idades)
                menor_idade = min(idades)
                
                print("\n--- RESULTADOS ---")
                print(f"a) Média de salário do grupo: R$ {media_salario:.2f}")
                print(f"b) Maior idade: {maior_idade} | Menor idade: {menor_idade}")
                print(f"c) Mulheres com salário >= R$ 5.000,00: {mulheres_5000}")
                input("Pressione Enter para continuar...")
                
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida! Tente 1, 2 ou 3.")

if __name__ == "__main__":
    main()
import os
os.system ("cls || clear")

while True: 
    print ("\n - Cardápio Menu -")
    print("\n 1 - Picanha")
    print ("2 - Lasanha")
    print ("3 - Strogonoff")
    print ("4 - Bife Acebolado")
    print ("5 - Pão com Ovo")

    codigo = int(input("\nPor Favor, escolha o código desejado: ")) 

    match codigo:
        case 1:
            print ("\nPicanha, 25,00.")
        case 2:
            print ("\nLasanha, 20,00.")
        case 3:
            print ("\nStrogonoff, 18,00.")
        case 4:
            print ("\nBife Acebolado, 15,00.")
        case 5:
            print ("\nPão com Ovo, 5,00.")
        case 6:
            print ("\nPrograma Encerrado.")
            break
              


            
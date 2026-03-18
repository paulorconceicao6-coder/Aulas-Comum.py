import os
import time

os.system ("cls || clear")

login_verdadeiro = "Paulo"
senha_verdadeira = "1997"
contador = 0

while True:
    login = input("Digite seu Login. ")
    senha = input("Digite a sua Senha. ")

    login_verdadeiro = login == login_verdadeiro
    senha_verdadeira = senha == senha_verdadeira
    
    if login_verdadeiro and senha_verdadeira:
        print ("\nLogin Realizado com Sucesso. ")
        break
    else:
        print ("\nSenha ou Login Incorretos, tente novamente.")
        tentativas += 1
        if tentativas == 3:
            print ("Número de Tentativas Excedido, tente novamente mais tarde. ")
            break


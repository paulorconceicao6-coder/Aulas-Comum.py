import os
import time
os.system ("cls || clear")

login = "paulo"
senha = "1997"

while True:
    login = input("\nDigite seu Login: ")
    senha = input("\nDigite a sua Senha: ")
    if login == "paulo" and senha == "1997":
        print ("\nAcesso Permitido. ")
        break
    else: 
        print ("\nLogin ou Senha Incorretos. ")

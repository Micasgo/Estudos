# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome

nome = str(input("Qual o seu nome? :")).strip()

if nome.lower().find("silva") != -1:
    print("Seu nome tem Silva")
else:
    print("Seu nome não tem Silva")
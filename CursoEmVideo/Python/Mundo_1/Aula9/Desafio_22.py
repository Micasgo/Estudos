#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome completo com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras tem ao todo sem considerar espaços
# Quantas letras tem o primeiro nome

nome = input(str("Digite seu nome: "))

print(nome.upper())
print(nome.lower())

print("Seu nome todo tem", len("".join(nome.strip().split())), "letras")

print("Seu primeiro nome tem",len(nome.split()[0]), "letras")
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.


nome = str(input("Qual o seu nome? :"))

print("Seu nome é", nome)
print("A primeira palavra é", nome.split()[0])
print("A última palavra é", nome.split()[::-1][0])
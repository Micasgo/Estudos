#Faça um programa que leia un número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: 1834
# Unidade: 4
# Dezena: 3
# Centena 8
# Milhar 1

num = str(input("Digite um número: "))

if len(num) == 1:
    print("Unidade:",num)

if len(num) == 2:
    print("Dezena: {}\nUnidade: {}".format(num[0],num[1]))

if len(num) == 3:
    print("Centena: {}\nDezena: {}\nUnidade: {}".format(num[0],num[1],num[2]))

if len(num) == 4:
    print("Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}".format(num[0],num[1],num[2],num[3]))
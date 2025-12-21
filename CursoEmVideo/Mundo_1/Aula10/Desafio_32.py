#  Faça um programa que leia um ano qualquer e
#  diga se ele é um ano bissexto

ano = int(input("Digite o ano a ser analizado: "))

if ano % 4 == 0:
    if ano % 100 == 0 and ano %400 == 0:
        print("O ano",ano, "é bissexto!")
        exit()
if ano % 4 == 0 and ano % 100 != 0:
    print("O ano", ano, "é bissexto!")
else:
    print("O ano", ano,"não é bissexto!")

# Desenvola um programa que leia as duas notas
#  de um aluno, calcule e mostre a sua média

n1 = int(input('Coloque sua primeira nota'))
n2 = int(input('Coloque sua segunda nota'))

média = (n1+n2)/2

#Bônus

if média > 10:
    print('Tá roubando, seu safado, de onde veio esses', média-10, 'pontos?')

if média >= 6 and média <= 10:
    print('Parabêns, você tirou {}'.format(média))

if média < 6:
    print('Você tirou {}, melhore'.format(média))
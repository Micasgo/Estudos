# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar. (Considerar U$$ == R$ 3,27)

real = float(input('Digite o dinheiro que você tem na carteira: R$'))
dol = real/3.27
euro = real/5.26

print('Com R${}, você consegue comprar US${:.2f}, ou EU{:.2f}.'.format(real,dol,euro))

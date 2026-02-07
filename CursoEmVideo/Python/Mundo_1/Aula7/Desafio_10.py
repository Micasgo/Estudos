# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar. (Considerar U$$ == R$ 3,27)

dinheiro = float(input('Quanto dinheiro você tem?'))
dólar = dinheiro/3.27
reais = dinheiro//1
centavos = (dinheiro-reais)*100

print('Com {} reais e {} centavos, você consegue comprar {:.2f} dólares.'
      .format(int(reais),int(centavos),dólar))
print(type(dinheiro))
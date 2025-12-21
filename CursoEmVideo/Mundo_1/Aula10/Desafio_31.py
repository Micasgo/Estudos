# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 para viagens mais longas

dist = float((str(input("Digite a distância da viagem em Km :"))).replace(",","."))

if dist <= 200:
    preço = dist*0.5
    print("Você terá que pagar R$0,50 por Km, portanto R${:.2f}".format(preço))
else:
    preço = dist*0.45
    print("Você terá que pagar R$0,45 por Km, portanto R${:.2f}".format(preço))

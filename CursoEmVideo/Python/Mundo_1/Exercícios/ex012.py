# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

vlr = float(input('Digite o preço do produto em R$: '))
desc = int(input('Digite o desconto do produto analisado. Digite o número da porcentagem :'))

descb = vlr*desc/100
vld = vlr-descb

print('De acordo com preço de R${}, com o desconto de {}%, o preço atualizado fica {:.2f}\no desconto foi de R${:.2f}'
      .format(vlr,desc,vld,descb))
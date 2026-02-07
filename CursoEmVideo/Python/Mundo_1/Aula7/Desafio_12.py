# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

price = float(input('Digite o preço'))
desc = float(input('Digite o desconto'))
priceB = price*desc/100
priceD = price-priceB


print("O preço de {} com {}% de desconto fica {:.2f}, um aumento de {:.2f}"
      .format(price,desc,priceD, priceB))
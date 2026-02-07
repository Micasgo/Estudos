"""
Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 50% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

produto = float(input("Digite o valor do produto a ser comprado: ").replace(",","."))

forma = input("Qual a forma de pagamento?\nDigite 1 para À vista (10% ou 5% de desconto, dinheiro ou cartão)\n"
              "Digite 2 para Parcelado\n:")

if forma == "1":
    avista = input("Para pagar à vista no cartão (5% de desconto) digite 1\n"
                   "Para pagar à vista no cheque/dinheiro/pix (10% de desconto) digite 2\n: ")
    if avista == "1":
        print(f"O preço ficará com o valor de \033[;32mR${produto*0.95:.2f}\033[m")
    elif avista == "2":
        print(f"O preço ficará com o valor de \033[;32mR${produto*0.9:.2f}\033[m")
    else:
        print("Opção Inválida")

elif forma == "2":

    print(f"2 parcelas terão o valor de \033[;32mR${(produto/2):.2f}\033[m")
    for i in range(10):
        print(f"{i+3} parcelas terão o valor de \033[;32mR${((produto*1.2)/(i+3)):.2f}\033[m")
    parcela = int(input("Parcelará em quantas vezes no cartão? (20% de juros a partir da 3° parcela)\n\n: "))
    print(f"O valor total será de {parcela} parcelas de \033[;32mR${produto*1.2/parcela:.2f}\033[m totalizando R${produto*1.2:.2f}")


else:
    print("Opção Inválida")

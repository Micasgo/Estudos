"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
"""
class cores:
    normal = 0
    negrito = 1
    vermelho = f'\033[0;31m'
    verde = f'\033[0;32m'
    reset = '\033[m'
    
def criar_aviso(texto=str, estilo=cores.normal, cor=cores.vermelho):
   
    print(f"{f'{cor}'.replace("0",str(estilo))}{texto}{cores.reset}")

valorCasa = float((input("Qual o valor da casa a ser comprada?: ")).replace(",",".").strip())

salario = float((input("Qual o seu salário?: ")).replace(",",".").strip())

duracao = int((input("Em quantos anos planeja pagar o valor da casa?: ")).strip())

limite = valorCasa / (duracao*12)

if limite > salario*0.3:
    print("\nQuer dar um golpe? Seu salário de não vai dar conta desse empréstimo\n")
    print("\n","=-="*10)
    criar_aviso("NEGADO".center(30),cores.negrito,cores.vermelho)
    print("","=-="*10,"\n")
    print(f'\n Suas prestações sairiam no valor de R${limite:.2f}')

else:

    print("\n","=-="*10)
    criar_aviso("Tudo certo!".center(30),cores.normal,cores.verde)
    print("","=-="*10,"\n")
    print(f'\n Suas prestações sairão no valor de R${limite:.2f}')

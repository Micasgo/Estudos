"""
Crie um programa que tenha a função leiaint(),
que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico
"""

def leiaint(mensagem):
    while True:
        num = input(f"{mensagem}: ").strip().replace(",",".")
        if num.isnumeric():
            num = int(num)
            return num
        else: print("Valor não reconhecido\n")


print(leiaint("Digite um número"))

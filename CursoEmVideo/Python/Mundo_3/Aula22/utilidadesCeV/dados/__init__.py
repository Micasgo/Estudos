"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com validaçãp de dados para aceitar apenas valores que sejam monetários.
"""

def leiaDinheiro():
    while True:
        din = input("Digite um valor monetário: ").strip().replace(",",".")
        if len(din) < 1:
            print("Valor não reconhecido")
        elif "." in din and len(din)<= 1:
                print("Valor não reconhecido")
        elif "." in din:
            din = float(din)
            break
        elif din.isnumeric():
            din = int(din)
            break
        else: print("Valor não reconhecido")
    return(din)
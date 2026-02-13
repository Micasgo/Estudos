"""
Reescreva a função leiaint() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

def leiaint(mensagem):
    try:
        num = int(input(f"{mensagem}: "))
    except (ValueError, TypeError):
        print("Houve um problema no tipo de dado que você digitou")
        num = 0
    except KeyboardInterrupt:
        print("O usuário preferiu não digitar o dado")
        num = 0
    return num

def leiaFloat(mensagem):
    try:
        num = float(input(f"{mensagem}: ").strip().replace(",","."))
    except (ValueError, TypeError):
        print("Houve um problema no tipo de dado que você digitou")
        num = 0
    except KeyboardInterrupt:
        print("O usuário preferiu não digitar o dado")
        num = 0
    return num

inte = leiaint("Digite um número inteiro")
real = leiaFloat("Digite um número real")

print(f"Número inteiro é {inte} e número real é {real}")

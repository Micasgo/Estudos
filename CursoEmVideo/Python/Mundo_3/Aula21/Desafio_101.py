"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa.
retornando um valorliteral indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
"""
def intinput(pergunta=str):
    while True:
        try:valor = int(input(f"{pergunta}: "))
        except ValueError: print("\nValor não reconhecido")
        else: break
    return valor

def voto(nascimento):
    global idade
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - nascimento
    if idade < 16: return "Voto \033[;33mNegado\033[m\n"
    elif 16 <= idade <= 17: return "Voto \033[;32mOpcional\033[m\n"
    elif 18 <= idade < 65: return "Voto \033[;31mObrigatório\033[m\n"
    else: return "Voto \033[;32mOpcional\033[m\n"

votacao = voto(intinput("Qual ano você nasceu?"))

print(f"Com {idade} anos, você tem {votacao}")

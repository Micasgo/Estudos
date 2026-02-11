"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "fim, o pragama se encerrará.
Obs: use cores.
"""
def escreva(mensagem="Lorem ipsum dolor sit amet", linha="-", cor = "\033[1;33;42m"):
    """Escreve uma mensagem separada por linhas

    Args:
        mensagem (str, optional): Corpo da mensagem. Defaults to "Lorem ipsum dolor sit amet".
        linha (str, optional): Forma da linha. Defaults to " ".
    """

    if len(linha) == 0: linha = " "
    fatorlinha = int(len(mensagem)/len(linha))//1+2
    borda = linha*fatorlinha
    print(cor)
    print(borda)
    print(mensagem.center(len(borda)))
    print(f"{borda}\033[m")

def PyHELP():
    from time import sleep
    escreva("Seja bem vindo ao PyHELP!","-=","\033[1;39;42m")
    sleep(1)
    while True:
        escreva("Digite a função desejada para o help (Digite FIM para terminar)","-","\033[7;31m")
        funcao = input()
        if funcao.lower() == "fim":
            break
        escreva(f"Pegando informações de {funcao}")
        sleep(1)
        print("\033[1;39;47m")
        help(funcao)
        print("\033[m")
        sleep(10)
    escreva("Terminando programa, volte sempre!")
        

PyHELP()

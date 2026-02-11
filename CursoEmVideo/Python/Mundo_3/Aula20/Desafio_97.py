"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva("Olá, Mundo!")
Saída:
-------------
 Olá, Mundo!
-------------
"""

def escreva(mensagem="Lorem ipsum dolor sit amet", linha="-"):
    """Escreve uma mensagem separada por linhas

    Args:
        mensagem (str, optional): Corpo da mensagem. Defaults to "Lorem ipsum dolor sit amet".
        linha (str, optional): Forma da linha. Defaults to " ".
    """

    if len(linha) == 0: linha = " "
    fatorlinha = int(len(mensagem)/len(linha))//1+1
    borda = linha*fatorlinha
    print(borda)
    print(mensagem.center(len(borda)))
    print(borda)

    

escreva("Funciona, que legal")

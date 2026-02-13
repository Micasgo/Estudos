def escreva(mensagem="Lorem ipsum dolor sit amet", linha="-", cor = f"\033[;;m",centrar = 0):
    """Escreve uma mensagem separada por linhas

    Args:
        mensagem: Corpo da mensagem. Padronizado como "Lorem ipsum dolor sit amet".
        linha: Forma da linha.
        cor: Escolhe uma cor para o print, padronizado como "033[m"
    """
    tamanho = len(linha)
    if tamanho == 0: linha = " "
    if centrar != 0: fatorlinha = int(centrar/tamanho)//1+2
    else: fatorlinha = int(len(mensagem)/tamanho)//1+2
    borda = linha*fatorlinha
    if "4" in str(cor): print(cor)
    else: print(cor,end="")
    print(borda)
    print(mensagem.center(len(borda)))
    print(f"{borda}\033[m")
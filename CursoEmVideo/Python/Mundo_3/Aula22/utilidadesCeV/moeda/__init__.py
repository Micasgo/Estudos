def moeda(valor):
    return f"R$ {valor}"

def aumentar(valor,aumento = 10,fmoeda = False):
    """Retorna um valor aumentado em x%.

    Args:
        valor (int): Valor a ser aumentado em x%.
        aumento (int): Porcentagem do aumento. Defaults to 10.
    """
    if fmoeda: return moeda(f"{(valor*(aumento/100+1)):.2f}")
    else: return f"{(valor*(aumento/100+1)):.2f}"

def diminuir(valor,diminuicao = 10,fmoeda = False):
    """Retorna um valor aumentado em x%.

    Args:
        valor (int): Valor a ser diminuido em x%.
        diminuicao (int): Porcentagem da diminuicao. Defaults to 10.
    """
    if fmoeda: return moeda(f"{(valor*(1-diminuicao/100)):.2f}")
    else: return f"{valor*(1-diminuicao/100):.2f}"

def dobro(valor, fmoeda = False):
    if fmoeda: return moeda(float(f"{(valor * 2):.2f}"))
    else: return f"{valor * 2:.2f}"

def triplo(valor, fmoeda = False):
    if fmoeda: return moeda(float(f"{(valor*3):.2f}"))
    else: return f"{(valor*3):.2f}"

def resumo(sal,aumento,desconto):
    from funcoes import grafico
    grafico.escreva("Resumo do Valor","=","\033[0;32m",centrar=45)
    print(f"Preço analisado: {(str(moeda(sal)).rjust(26,"."))}")
    print(f"Com {aumento}% de aumento fica {aumentar(sal,aumento, True).rjust(21,".")}")
    print(f"Com {desconto}% de desconto fica {diminuir(sal,desconto, True).rjust(20,".")}")
    print(f"O dobro é {dobro(sal, True).rjust(34,".")}")
    print(f"O triplo é {triplo(sal, True).rjust(33,".")}")
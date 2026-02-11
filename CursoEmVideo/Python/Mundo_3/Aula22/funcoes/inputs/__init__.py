def perguntaPolar(pergunta="", A="S", B="N"):
    """Faz um input e retorna um opção dicotômica, primeira letra em maiúsculas de uma alternativa A ou B.
    Trata os erros caso o usuário não digite a opção definida.

    :param pergunta: Corpo da mensagem
    :param A: Primeira Alternativa, padrão "S"
    :param B: Segunda Alternativa, padrão "N"
    """
    while True:
        try:
            while True:
                condicao = input(f"{pergunta} ({A.upper()}/{B.upper()}): ").strip().upper()[0]
                if condicao not in (A+B): print("\nOpção Inválida")
                else: break
        except IndexError: print("\nValor não reconhecido")
        else: break
    return condicao

def numinput(pergunta="Digite um número",opcao = int):
    """Não retorna erro caso o input não seja um int, retorna um print "Valor não reconhecido"
    Para usar float, utilize opcao= float

    :param pergunta: Corpo da mensagem
    """
    while True:
        try:valor = opcao(input(f"{pergunta}: ").strip().replace(",","."))
        except ValueError: print("\nValor não reconhecido")
        else: break
    return valor

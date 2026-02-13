def cadastro():
    from funcoes import inputs, grafico
    grafico.escreva("Cadastrando Pessoa","=","\033[;32m",40)

    nome = input("Qual o nome da pessoa?")
    idade = inputs.numinput(f"Digite a idade de {nome}")
    with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"a",encoding="utf-8") as txt:
        txt.write(f"{nome:<35}{idade:>3}")
        txt.write("\n")

def ler():
    from funcoes import grafico
    try:
        grafico.escreva("""             Lendo Cadastrados
N° | Nome                          |Idade""","=","\033[;32m",40)
        with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"r",encoding="utf-8") as txt:
            for pos, linha in enumerate(txt.readlines()):
                print(f"n°{pos+1} {linha}",end="")
    except FileNotFoundError:
        txt = open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"w",encoding="utf-8")
        txt.close()
    
def delete():
    from funcoes import inputs
    try:
        ler()
        apagar = inputs.numinput("\033[;31mEscolha a linha para apagar\033[m: ")-1
        with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"r",encoding="utf-8") as txt:
            linhas = list(l for l in txt.readlines())
        with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"w",encoding="utf-8") as txt:
            for pos, l in enumerate(linhas):
                    if pos != apagar:
                        txt.write(l)
                        txt.write("")
    except FileNotFoundError:
        txt = open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"w",encoding="utf-8")
        txt.close()

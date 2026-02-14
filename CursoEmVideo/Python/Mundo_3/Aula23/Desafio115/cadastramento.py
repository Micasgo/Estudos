def cadastro():
    from funcoes import inputs, grafico
    grafico.escreva("Cadastrando Pessoa","=","\033[;32m",40)

    nome = input("Qual o nome da pessoa?")
    idade = inputs.numinput(f"Digite a idade de {nome}")
    with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"r",encoding="utf-8") as txt:
        tamanho = len(txt.readlines())

    with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"a",encoding="utf-8") as txt:
        if tamanho == 0: txt.write(f"{nome};{idade}")
        else: txt.write(f"\n{nome};{idade}")

def ler():
    from funcoes import grafico
    try:
        grafico.escreva("""             Lendo Cadastrados
N° | Nome                          |Idade""","=","\033[;32m",40)
        with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"r",encoding="utf-8") as txt:
            for pos, linha in enumerate(txt.readlines()):
                try: 
                    cont = linha.split(";")
                    print(f"n°{pos+1:<2} {cont[0]:<34}{cont[1]:>4}",end="")
                except: print(f"n°{pos+1:<2} Linha Vazia")
                
    except FileNotFoundError:
        txt = open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"w",encoding="utf-8")
        txt.close()
    
def delete():
    from funcoes import inputs
    try:
        ler()
        apagar = inputs.numinput("\033[;31m\nEscolha a linha para apagar\033[m: ")-1
        with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"r",encoding="utf-8") as txt:
            linhas = list(l for l in txt.readlines())
        with open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"w",encoding="utf-8") as txt:
            for pos, l in enumerate(linhas):
                    if pos != apagar:
                        txt.write(l)
                    if l != linhas[-1]:
                        txt.write("")
    except FileNotFoundError:
        txt = open(r'C:\Users\MICAS\Documents\GitHub\Estudos\CursoEmVideo\Python\Mundo_3\Aula23\Desafio115\Pessoas.txt',"w",encoding="utf-8")
        txt.close()

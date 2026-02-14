"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas
pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar e uma nova pessoa e listar todas as pessoas cadastradas
"""

from funcoes.grafico import escreva
from funcoes import inputs
import cadastramento

escreva("Bem vindo ao Cadastramento","=","\033[;32m",40)

while True:
    print()
    escreva("""1- Cadastrar
2- Ler Cadastrados
3- Deletar Linha
4- Sair do programa""","=","\033[;33m",40)
    while True:
        opcao = inputs.numinput("Digite a opção desejada")
        if not 1 <= opcao <= 4: print("Opção Inválida")
        else: break

    if opcao == 1:
        cadastramento.cadastro()
    elif opcao == 2: cadastramento.ler()
    elif opcao == 3: cadastramento.delete()
    elif opcao == 4:
        escreva("Fim do Programa","=","\033[;32m",40)
        break

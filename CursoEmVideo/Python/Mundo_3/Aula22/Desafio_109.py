"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
"""

from utilidadesCeV import moeda
from funcoes import inputs

sal = inputs.numinput("Qual o seu salário?",opcao=float)
aumento = inputs.numinput("Qual a porcentagem do aumento?")
desconto = inputs.numinput("Qual a porcentagem do desconto?")

print(f"Preço analisado: {(str(moeda(sal)).rjust(26,"."))}")
print(f"Com {aumento}% de aumento fica {moeda.aumentar(sal,aumento, True)}")
print(f"Com {desconto}% de desconto fica {moeda.diminuir(sal,desconto, True)}")
print(f"O dobro é {moeda.dobro(sal, True)}")
print(f"O triplo é {moeda.triplo(sal, True)}")
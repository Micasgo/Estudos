"""
Adicione ao módulo moeda.py criado nos desafios anteriores uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

from utilidadesCeV import moeda
from funcoes import inputs

sal = inputs.numinput("Qual o seu salário?",opcao=float)
aumento = inputs.numinput("Qual a porcentagem do aumento?")
desconto = inputs.numinput("Qual a porcentagem do desconto?")

moeda.resumo(sal,aumento,desconto)
"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com validaçãp de dados para aceitar apenas valores que sejam monetários.
"""

from utilidadesCeV import moeda, dados
from funcoes import inputs

sal = dados.leiaDinheiro()
aumento = inputs.numinput("Qual a porcentagem do aumento?")
desconto = inputs.numinput("Qual a porcentagem do desconto?")

moeda.resumo(sal,aumento,desconto)

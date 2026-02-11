"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro e metade()
Faça também um programa que importe e sse module e use algumas dessas funções
"""
from utilidadesCeV import moeda
from funcoes import inputs

sal = inputs.numinput("Qual o seu salário?",opcao=float)
porcento = desconto = inputs.numinput("Qual a porcentagem para a análise?")

print(f"Caso aumente será R$ {moeda.aumentar(sal,porcento)}")
print(f"Se diminuir será R$ {moeda.diminuir(sal,porcento)}")
print(f"O dobro é {moeda.dobro(sal)}")
print(f"O triplo é {moeda.triplo(sal)}")
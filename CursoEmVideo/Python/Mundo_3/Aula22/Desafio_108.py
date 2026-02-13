"""
Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar
os valores como um valor monetário formatado
"""
from utilidadesCeV import moeda
from funcoes import inputs

sal = inputs.numinput("Qual o seu salário?",opcao=float)
porcento = inputs.numinput("Qual a porcentagem para a análise?")

print(f"Caso aumente será {moeda.moeda(moeda.aumentar(sal,porcento))}")
print(f"Se diminuir será {moeda.moeda(moeda.diminuir(sal,porcento))}")
print(f"O dobro é {moeda.moeda(moeda.dobro(sal))}")
print(f"O triplo é {moeda.moeda(moeda.triplo(sal))}")
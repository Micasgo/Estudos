"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

lista_pessoas = []
hmaisvelhoi = -1
hmaisvelhon = "Não há"
mulheres = 0
soma_idade = 0

pessoas = int(input("Quantas pessoas serão analisadas?: "))

for i in range(pessoas):
    print(f"\n-=-=-=- {i+1}° Pessoa -=-=-=-\n")
    nome = input(f"Qual o nome?: ").strip()
    idade = int(input(f"Qual a idade?: ").strip())
    sexo = input(f"Qual o sexo? (M/F):").strip().upper()[0]

    pessoa = {"nome": nome, "idade": idade, "sexo": sexo}
    lista_pessoas.append(pessoa)

    soma_idade += idade

    if sexo == 'M':
        if hmaisvelhoi < idade:
           hmaisvelhoi = idade
           hmaisvelhon = nome
    else:
        if idade < 20:
            mulheres += 1

print(f"A média das idades é de {soma_idade/pessoas:.1f}")

print(f"O nome do homem de maior idade é {hmaisvelhon}, que tem {hmaisvelhoi} anos")

print(f"No grupo há {mulheres} mulher(es) abaixo de 20 anos")

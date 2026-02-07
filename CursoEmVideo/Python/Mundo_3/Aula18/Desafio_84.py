"""
Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
maior = menor = cont = 0
grupo = []
pessoa = []

def perguntaSN(pergunta=str):
    while True:
        try:
            while True:
                condicao = input(f"\n{pergunta} (S/N): ").strip().upper()[0]
                if condicao not in "SN": print("\nOpção Inválida")
                else: break
        except IndexError: print("\nValor não reconhecido")
        else: break
    return condicao

while True:
    cont += 1
    print(f"{cont}° pessoa".center(20),'\n',"-="*10)
    nome = input(f"Qual o nome?: ")
    while True:
        try:
            peso = float(input("Qual o peso em kg?: ").strip().replace(",","."))
        except ValueError:
            print("Valor não reconhecido")
        else: break
    pessoa.append(nome)
    pessoa.append(peso)
    grupo.append(pessoa[:])
    
    condicao = perguntaSN("Deseja continuar?")

    if cont == 1:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior: maior = pessoa[1]
        elif pessoa[1] < menor: menor = pessoa[1]
    pessoa.clear()
    if condicao == "N": break

print("\n","-="*10,f"\nExistem {len(grupo)} pessoas no total")

print(f"O maior peso é {maior}kg, em: ",end="")
for p in grupo:
    if p[1] == maior:
        print(p[0],end=", ")
print()
print(f"O menor peso é {menor}kg, em: ",end="")
for p in grupo:
    if p[1] == menor:
        print(p[0],end=", ")



#maior = max(p[1] for p in grupo)
#menor = min(p[1] for p in grupo)
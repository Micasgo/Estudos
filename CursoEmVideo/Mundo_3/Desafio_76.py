"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

tupla = ("Sabão",12.99,"Carne",44.59,"Pão",4.60,"Notebook",2499.99,"RTX 5060",1999.99,"Curso em Vídeo",0.00,"Oculus Quest 3s",2259.99)

print(f"\n{'TABELA DOS PRODUTOS':^45}\n")
print("-="*25)
for pos, i in enumerate(tupla):
    if pos % 2 == 0:
        print(f"{i:.<40}",end="")
    elif pos % 2 != 0:
        print(f"R$",f"{i:.2f}".rjust(7))
print("-="*25)

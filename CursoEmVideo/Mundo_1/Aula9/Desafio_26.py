# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela última vez

frase = str(input("Digite uma frase :")).strip()

print('A letra "A", aparece nessa frase {} vezes'
      .format(frase.upper().count("A")))
print("A letra aparece pela primeira vez na posição",frase.lower().find("a")+1)
print("A letra aparece pela última vez na posição",frase.lower().rfind("a")+1)
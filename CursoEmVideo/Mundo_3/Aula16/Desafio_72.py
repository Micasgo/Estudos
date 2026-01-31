"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
Seu programa ddeverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

extenso = (
           "zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze",
           "Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte"
          )
while True:
    num = int(input("Qual número você quer por extenso? (0 à 20): "))
    if not 0 < num < 20:
        print("\nNúmero não aceito\n")
    else:
        break

print(f"O número {num} em extenso é: {extenso[num]}")

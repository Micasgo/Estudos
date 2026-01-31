"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso você deve mostrar, para cada palavra, quais são as suas vogais.
"""
tupla = ("Abacaxi","Carro","McQueen","Mate","Tomate","Barganha","Doutor","Louco","Willem Dafoe","Nova Iorque")

for palavra in tupla:
    print(f"As vogais da palavra {palavra} é: ",end="")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra.lower(),end=" ")
    print("")

palavra = input("Coloque uma palavra para ser analizada: ")
palavra_f = palavra.replace(" ","").lower()

if palavra.find(" ") != -1:
    print("Eu disse palavra, não frase, mas tudo bem\n\n")

if palavra_f == palavra_f[::-1]:
    print("Sua palavra é um palíndromo")
else:
    print("Sua palavra não é um palíndromo")

print(palavra_f[::-1])
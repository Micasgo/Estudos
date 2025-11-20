#Crie um programa que leia  o nome de uma cidade e diga se ela começa com o nome "SANTO"

cidade = str(input("Escreva o nome da cidade: "))

if cidade.split()[0].lower().find("santo") == 0:
    print("A cidade começa com santo")
else :
    print ("A cidade não começa com santo")
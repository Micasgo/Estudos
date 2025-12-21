import random

frase = "Curso de Python"

valor = frase.split()

valor = random.sample(valor, 3)

retorno = " ".join(valor)

print(retorno)
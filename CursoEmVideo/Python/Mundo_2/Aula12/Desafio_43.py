"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu IMC e
mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input("Qual o seu peso em Kg? :").replace(",","."))
altura = float(input("Qual sua altura em metros?: ").replace(",","."))

imc = peso/altura**2

print(f"Seu índice de massa corporal possui o valor de {imc:.1f}")

if imc < 18.5:
    print("\033[;33mAbaixo do peso\033[m")
elif imc >= 18.5 and imc <= 25:
    print("\033[;32mPeso ideal\033[m")
elif imc > 25 and imc <= 30:
    print("\033[;33mSobrepeso\033[m")
elif imc > 30 and imc <= 40:
    print("\033[1;31mObsidade\033[m")
elif imc > 40:
    print("\033[;31mObesidade Mórbida\033[m")

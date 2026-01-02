class carro:
    material = "aço"

    def __init__(self,modelo, fabricação):
        
        self.modelo = modelo
        self.fabricação = fabricação

    def acelerar(self):

        return f"Seu {self.modelo} está acelerando desde {self.fabricação}"
    
    def idade(self):

        return f"Seu carro já tem {2025-int(self.fabricação)} anos."
    
modelo = input("Qual o modelo do seu carro?")

fabricação = input("Qual o ano que seu carro foi fabricado?")

carro1 = carro(modelo,fabricação)

print(carro1.acelerar())

print(f"Carro é feito de {carro.material}")

print(carro1.idade())
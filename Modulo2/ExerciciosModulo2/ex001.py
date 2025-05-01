# Exercicio 1
class Pedidos():
    def __init__(self, *pedidos): # Aceitando argumentos variáveis para comidas 
        self.pedido = list(pedidos) # Convertendo para lista 


joaquim = Pedidos("Feijão com farinha", "Arroz", "Bife")
print(f"O seu pedido foi: {joaquim.pedido}")

class Bebidas(Pedidos):
    def __init__(self, *bebidas):
        super().__init__(*bebidas)

        self.bebidas = list(bebidas)

joaquim = Bebidas("Refrigerante")
print(f"Você pediu para beber: {joaquim.bebidas}")

# Exercicio 2 
class Animal():
    def __init__(self, nome, raca):
        self.nome = nome 
        self.raca = raca 

    def correr(self):
        return f"{self.nome} está correndo por aí"
        
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)
    
    def latir(self):
        return f"{self.nome} não para de latir! Au Au AUUUU"
    

puddle = Cachorro("Rex", "Puddle")
print(puddle.correr())
print(puddle.latir())
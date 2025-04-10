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
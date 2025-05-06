"""
Criar um sistema simples que represente diferentes meios de transporte. 
Cada meio de transporte deve ser uma sub-classe de uma classe base chamada 
Transporte. 
"""
class Transporte():
    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        raise NotImplementedError("Subclasses deve implementar esse método")

class Carro(Transporte):
    def mover(self):
        return f"{self.nome} está andando pela estrada, vruuum 🚗"

class Bicicleta(Transporte):
    def mover(self):
        return f"{self.nome} está pedalando pela ciclovia 🚲"
    
class Moto(Transporte):
    def mover(self):
        return f"{self.nome} está rodando numa via vazia, que maravilha 🏍️"
    
v1 = Carro("Fiat Uno")
v2 = Bicicleta("Caloi")
v3 = Moto("Yamaha")

for nome in [v1, v2, v3]:
    print(nome.mover())



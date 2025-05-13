class Escritor:
    def __init__(self, nome) -> None :
        self.nome = nome
        self._ferramenta = None

    @property 
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter 
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class Ferramenta_de_escrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f"{self.nome} está escrevendo" 
    
escritor = Escritor("Luiz")
caneta = Ferramenta_de_escrever("Caneta Bic")
escritor.ferramenta = caneta # Associando o objeto escritor ao objeto ferramenta de escrever

print(caneta.escrever())
print(escritor.ferramenta.escrever()) 
        
        
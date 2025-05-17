"""
Associação:
É o conceito mais geral e abrange qualquer tipo de relacionamento entre objetos de diferentes 
classes. ***Não implica em uma dependência forte*** entre as classes envolvidas, ou seja, 
uma classe pode referenciar outra, mas elas podem existir independentemente uma da outra. 
A associação pode ser **unidirecional** (onde uma classe conhce a outra) ou **bidirecional** 
(onde ambas as classes se conhecem).
Esses conceitos são essenciais em POO porque ajudam a modelar a **vida e a dependência** 
entre os objetos, permitindo a criação de sistemas mais organizados e com menos acoplamento 
entre classes.

Agregação:
É uma forma especial de associação, um tipo de relacionamento entre classes onde um objeto "Pai" 
contém ou "possui" um objeto "Filho", mas o objeto "Filho" pode existir de forma independente do 
objeto "Pai". Ou seja, o ciclo de vida do objeto "Filho" não depende do objeto "Pai". 
O objeto "Filho" pode ser compartilhado entre diferentes objetos "Pais" 
e pode existir fora do contexto do objeto "Pai" que o contém.

**Exemplo**: Uma **biblioteca** pode agregar muitos **livros**, 
mas os **livros** podem existir sem a **biblioteca**.


Composição:
É um tipo mais forte de agregação, onde um objeto "Pai" contém ou "possui" um objeto "Filho" 
e o ciclo de vida do objeto "Filho" depende diretamente do objeto "Pai". Ou seja, se o 
objeto "Pai" for destruído, o objeto "Filho" também será destruído. Os objetos "Filhos" não fazem 
sentido sem o objeto "Pai", ou seja, eles não podem existir independentemente.

**Exemplo**: Um **carro** possui um **motor**, mas não pode existir sem o **carro**; 
se o **carro** for destruído, o **motor** também será

ASSOCIAÇÃO --> AGREGAÇÃO --> COMPOSIÇÃO
"""

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
        
        
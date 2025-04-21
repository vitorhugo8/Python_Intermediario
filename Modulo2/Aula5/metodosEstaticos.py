"""
@staticmethod (métodos estáticos) são inúteis em Python :P

É uma funcionalidade comum em algumas linguagens de programação (como C++ e Java por exemplo) que permitem
definir métodos que podem ser chamados em uma classe sem a necessidade de uma instância da classe.
Este método não tem acesso a self e nem a cls.
"""
# MÉTODO ESTÁTICO (staticmethod)
# Um método que não recebe nem self e nem cls como argumentos. Ele não tem acesso nem a instância e nem a classe, ou seja, 
# ele é basicamente um método "normal", mas definido dentro da classe. 

class Classe:
    @staticmethod
    def funcao_classe(*args):
        for item in args:
            print("Olá, eu sou um método de uma classe estática")
        
c1 = Classe()
c1.funcao_classe(1, 2, 3)

# MÉTODO NORMAL (instãncia)
# Um método de instância é aquele que opera sobre uma instância de uma classe. 
# Quando criamos uma classe, o primeiro método de instância é o self, que é uma referência à instância da classe. 
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo 
        
    def exibir_modelo(self): # Método de instância - pode ser usado como instância de classe
        print(f"O modelo do carro e: {self.modelo}")

carro = Carro("fusca")
carro.exibir_modelo()

# CLASSMETHOD (método de classe)
# É um método que recebe a classe como primeiro argumento, ao invés de uma instãncia. 
# Por convenção, esse argumento é chamado de 'cls'. 
class Fruta:
    cesta_de_frutas = 0
    
    def __init__(self, frutas):
        self.frutas = frutas 
        Fruta.cesta_de_frutas += 1
    
    @classmethod # Pode ser chamado sem uma instância 
    def total_frutas(cls):
        print(f"O total de frutas na cesta é de: {cls.cesta_de_frutas}")
        

Fruta.cesta_de_frutas 
pera = Fruta("pêra")
maca = Fruta("maçã")
Fruta.total_frutas()
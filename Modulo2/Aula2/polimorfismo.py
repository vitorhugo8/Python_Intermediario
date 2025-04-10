"""
Polimorfismo é uma característica de linguagens orientadas a objetos, que permite que 
diferentes objetos respondam a mesma mensagem cada um a sua maneira. 

Classe Abstrata - É uma classe que não pode ser instãnciada diretamente, mas que serve 
como base para outras classes. Ela funciona como o escopo de outras classes.

Interface - É um conjunto de métodos que uma classe deve implementar. Ela define o 
comportamento de uma classe sem fornecer detalhes de implementação.

"""
"""
A Interface: 
suporta herança múltipla, 
permite apenas métodos abstratos, 
não contém atributos,
Não contém construtor.

A Classe Abstrata: 
Não suporta herança múltipla, 
Pode conter atributos de todos os tipos,
Contém construtor.

"""
# Exemplo de classe abstrata (utilziando o módulo abc)
from abc import ABC, abstractmethod # Decorador utilizado para definir métodos abstratos

class Animal(ABC): # Classe abstrata, com o método abstrato 'fazer_som'
    @abstractmethod
    def fazer_som(self):
        pass

# Cachorro e Gato herdam a classe Animal (como estudamos em herança) e implementam o método 'fazer_som'
class Cachorro(Animal): 
    def fazer_som(self):
        return "au au!"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
    
# Exemplo de Interface em Python 
"""Python não tem interface nativa como Java ou C#, mas a classe abstrata com
somente métodos abstratos pode simular o comportamento de uma interface"""
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass 

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2
    
# Como Quadrado e Círculo implementam calcular_area, eles podem ser tratados polimorficamente
# como Forma 
def imprimir_area(forma: Forma):
    print(f"A área é: {forma.calcular_area()}")

formas = [Quadrado(4), Circulo(3)]

for forma in formas: # Para cada forma dentro da lista de formas, chamamos a função 'imprimir_area'
    imprimir_area(forma)

        
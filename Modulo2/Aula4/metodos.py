"""
Métodos de Classe + Factories (fábricas)
São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro
receberemos a própria classe.

Em Python, Factories são padrões de projeto que te permitem criar objetos sem especificar a classe
exta do objeto 

Exemplo -- Imagine um sistema que precisa criar diferentes tipos de carros. Em vez de ter diferentes 
classes para cada tipo de carro, uma fábrica pode ter um método que, 
com base em um parâmetro (ex: "esportivo", "familiar"), retorna o carro correspondente. 
"""
class Pessoa():
    ano = 2025 # Exemplo de atributo de classe 

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # Permite que você chame a classe sem utilizar o 'self'
    def metodoClasse(cls):
        print("Hey")

    @classmethod # Decorador
    def criarCom50Anos(cls, nome):
        return cls(nome, 50) # Hard Coded 
        # O cls representa a classe em si, e não uma instância

p1 = Pessoa("Anônima", 23)
print(p1.nome, p1.idade)


"""
Métodos de Classe.
São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro
receberemos a própria classe.
"""
class Pessoa():
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodoClasse(cls):
        print("Hey")

    @classmethod # Decorador
    def criarCom50Anos(cls, nome):
        return cls(nome, 50) # Hard Coded 
        # O cls representa a classe em si, e não uma instância

p1 = Pessoa("João", 34)
p2 = Pessoa.criarCom50Anos("Maria")
print(p2.nome, p2.idade)


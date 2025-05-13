"""
__dict__ e vars para atributos de instância.
  dict em Python é uma estrutura de dados que armazen pares de chave-valor,
  permitindo a recuperação eficiente de dados. 
    
  Um par cave-valor é uma estrutra de dados que associa uma chave a um valor. 
  A chave identifica o valor (que pode ser um int, str, objeto ou qualquer outro tipo de dado)
  
"""
class Pessoa():
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade 
    
p1 = Pessoa("João", 35)
print(p1.__dict__) # Retorna os valores de instância com os nomes (Nome: "João", Idade: "35")
"""
method x @classmethod x @staticmethod

1. Método de Instância (method)
    Definido normalmente com 'def' dentro de uma classe. 
    Recebe o primeiro argumento como 'self', que é a instância atual do objeto.
    Pode acessar e modificar atributos da Instância. 

2. Método de classe (@classmethod)
    Recebe o primeiro argumento como 'cls', que representa a própria classe (não a
    instância).
    Usado, por exemplo, para criar instâncias alternativas ou acessar/modificiar dados
    da classe.

3. Método estático (@staticmethod)
    Decorado com '@staticmethod'.
    Não recebe automaticamente 'self' nem 'cls'.
    Funciona como uma função comum dentro da classe.
    Usado quando o método não depende da instância nem da classe, mas faz sentido
    semanticamente estar dentro da classe. 
    (Provalvavelmente, eu não vou usar muito).
"""
# Exemplo de method 
class Pessoa:
    def __init__(self, nome):
        self.nome = nome 

    def saudacao(self):
        return f"Olá {self.nome}, eu sou o seu computador!"

p = Pessoa("João")
print(p.saudacao())

# Exemplo de @classmethod
class Pessoa:
    especie = "Humano"

    def __init__(self, nome):
        self.nome = nome 
    
    @classmethod
    def especie_da_classe(cls):
        return f"Todos são da espécie: {cls.especie}"
    
print(Pessoa.especie_da_classe())

# Exemplo de @staticmethod 
class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b 
    
print(Calculadora.somar(2, 2))
        
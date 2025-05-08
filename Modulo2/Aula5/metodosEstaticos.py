"""
@staticmethod (métodos estáticos) são inúteis em Python :P

É uma funcionalidade comum em algumas linguagens de programação (como C++ e Java por exemplo) 
que permitem definir métodos que podem ser chamados em uma classe 
sem a necessidade de uma instância da classe.
Este método não tem acesso a self e nem a cls.

"""
# MÉTODO ESTÁTICO (static method)
# Um método que não recebe nem self e nem cls como argumentos. Ele não tem acesso nem a instância 
# e nem a classe, ou seja, ele é basicamente um método "normal", mas definido dentro da classe. 

class Classe:
    @staticmethod
    def funcao_classe(*args):
        for item in args:
            print("Olá, eu sou um método estático de uma classe!")
        
c1 = Classe()
c1.funcao_classe(1, 2, 3)


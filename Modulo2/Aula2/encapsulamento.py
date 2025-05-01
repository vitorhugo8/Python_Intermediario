"""
O encapsulamento é um princípio fundamental na Programação Orientada a Objetos. 
Este princípio diz que uma classe filha pode herdar propriedas e/ou métodos de uma classe pai. 
Isto nos permite reutilizar códigos, evita exclusões acidentais e protege as classes contra alterações.

OBS: Em outras linguagens OOP, como Java e C++, o encapsulamento é estritamente imposto com modificadores de acesso, 
como public, private ou protected, mas o Python não tem isso

"""
# Exemplo 1
class Smartphone():
    def __init__(self, brand, os):
        self.brand = brand 
        self.os = os

iphone = Smartphone("Apple", "IOS 17") # Com ambos os atributos públicos, qualquer pessoa pode modificar. Por exemplo, podem fazer um Apple rodar num sistema operacional Android
# print(iphone.os)


# Exemplo 2
class Celular():
    def __init__(self, modelo, so):
        self.modelo = modelo 
        self._so = so
        """ Com esse underline ao lado do 'so' deixamos claro para os desenvolvedores 
            que virem este código, que a propriedade de so não pode ser alterada a qualquer momento,
            mas se eles quiserem, ainda podem modificar
        """

xiaomi = Celular("Xiaomi", "Hyper OS")
print(xiaomi.modelo)
print(xiaomi._so)


# Exemplo 3 
class Livro():
    def __init__(self, nome_livro ,autor, n_de_paginas):
        self.nome_livro = nome_livro
        self.__autor = autor
        self.n_de_paginas = n_de_paginas

domCasmurro = Livro("Dom Casmurro", "Machado de Assis", 384) 
print(domCasmurro.__autor) # AtributeError: 'Livro' object has no attribute '__autor'

""" O código mostra uma mensagem de erro, ou seja, este atributo não pode ser alterado e muito
menos acessado por qualquer pessoa. """
        
        
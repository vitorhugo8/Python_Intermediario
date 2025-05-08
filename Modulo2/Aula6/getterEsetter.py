"""
@property - Um getter no modo Pythônico

getter (acessador) - Um método para obter um atributo privado de uma classe. 
Ele não altera o estado do objeto, apenas retorna o valor do atributo.

Geralmente é usado nas seguintes situações: 
    p/ evitar quebra de código do cliente, 
    p/ habilitar 'setter',
    p/ executar ações ao obter um atributo. 
    ...

OBS: Código Clinte é o código que usa o seu código 
"""
class Caneta:
    def __init__(self, cor="Preta"):
        self.__cor = cor # Atributo privado 
    
    def get_cor(self): # Método de acesso (getter)
        return self.__cor
    
    def set_cor(self, nova_cor): # Método de setter: modifica o valor
        self.__cor = nova_cor

# Acessando a cor padrão da caneta através do método getter
caneta1 = Caneta()
print(caneta1.get_cor())

# Mudando a cor da caneta modificando o atributo diretamente (sem mudar a cor padrão) 
caneta2 = Caneta("Azul")
print(caneta2.get_cor())

# Usuário 2 decide trocar de caneta 
caneta2.set_cor("vermelha")
print(caneta2.get_cor())

# A primeira caneta continua sendo preta 
print(caneta1.get_cor())
        
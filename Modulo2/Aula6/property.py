"""
Decorators - Uma função decorator é, basicamente, uma função que adiciona uma nova 
funcionalidade a uma função pre-existente, que é passada como argumento. Ela dá uma nova 
funcionalidade a uma função existente sem modificá-la.

Por que usar o Property? 
    Torna os métodos de acesso mais naturais:
        Você escreve 'caneta.cor', não 'caneta.get_cor()'
        Você atribui caneta.cor = 'vermelha', não set_cor('vermelha')

    Fica mais limpo, legível e elegante, mas ainda permite controle e validação por trás 
    dos panos.
    Vocẽ pode transformar um atributo público simples em um método mais tarde sem mudar o jeito
    que o código é usado. 
    
"""
# Exemplo de uso de property 
class Caneta: 
    def __init__(self, cor="Preta"):
        self.__cor = cor 

    @property # Mostra a cor da caneta 
    def cor(self):
         return self.__cor 

    @cor.setter # Altera a cor da caneta, sem precisar acessar um método diretamente
    def cor(self, nova_cor):
        self.__cor = nova_cor 

# Uso do getter 
caneta1 = Caneta()
print(caneta1.cor) # Acessando como atributo, mas é um método por trás 

caneta2 = Caneta("Azul")
print(caneta2.cor)

print(caneta1.cor) # Sem alterar a cor da caneta original 
        
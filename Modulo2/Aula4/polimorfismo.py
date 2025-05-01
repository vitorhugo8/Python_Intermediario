"""
Polimorfismo refere-se a capacidade dos objetos diferentes de se comportar de maneira semelhante as mesmas 
mensagens. Isso facilita o desenvolvimento de software mais flexível, reutilizável e fácil de manter.
"""

class Funcionario():
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
        

class Vendedor(Funcionario):
    def __init__(self, nome, funcao):
        super().__init__(nome, funcao)

    def calcular_salario(self):
        salario = 2000 - ((300 - 20 - 40)/2) 
        return round(salario)
    
carlos = Vendedor("Carlão", "Vendedor")
print(f"O salário do {carlos.funcao} é de: R${carlos.calcular_salario()}")
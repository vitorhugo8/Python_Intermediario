"""
Polimorfismo refere-se a capacidade de múltiplas classes de terem métodos com o 
mesmo nome, mas com comportamentos diferentes. Isso permite que objetos de diferentes
classes possam ser tratados de forma uniforme, geralmente por meio de uma interface
comum ou classe base. 
"""

class Funcionario():
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
    
    def calcular_salario(self):
        raise NotImplementedError("Subclasses deve implementar esse método")
        # Função que obriga as sub-classes a utilizarem esse método se herdarem da classe 'Funcionario'
        
class Vendedor(Funcionario):
    def calcular_salario(self):
        salario = 2000 - ((300 - 20 - 40)/ 2)
        return round(salario)
    
class Gerente(Funcionario):
    def calcular_salario(self):
        return 5000

# Uso polimorfico 
def imprimir_salario(Funcionario):
    print(f"O salário do {Funcionario.funcao} é de R${Funcionario.calcular_salario()}")

carlos = Vendedor("Carlos", "Vendedor")
ana = Gerente("Ana", "Gerente")

for pessoa in [carlos, ana]:
    imprimir_salario(pessoa)
 
    
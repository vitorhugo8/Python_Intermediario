"""
A Herança permite que uma clase herde atributos e métodos de outra classe, facilitando
a reutilização. 

Por exemplo, quando criamos um código de cadastro. Podemos reutilizar atributos 
em comum entre os usuários para cadastrá-los no nosso sistema.

Quando herdamos uma classe, não nos limitamos aos métodos e atributos dela. 
Nossas subclasses podem ter atributos e métodos específicos. 
A proposta da herança é reaproveitar métodos e atributos em comum.

"""
# Exemplo do uso de Herança 
class Veiculo:
    def __init__(self, marca, modelo, qtd_rodas):
        self.marca = marca
        self.modelo = modelo 
        self.qtd_rodas = qtd_rodas
    
    def acelerar(self):
        print(f"O {self.marca} está acelerando vruuum")

    def frear(self):
        print("O veículo está freando")

    def mudar_direcao(self, direcao):
        if direcao == "esquerda":
            print("Virando o veículo para a esquerda")
        elif direcao == "direita":
            print("Virando o veículo para a direita")
        else:
            print("Seguindo em frente")
# honda = Veiculo("Honda", "Civic", 4)    
# honda.acelerar()
# honda.frear()

class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_rodas, tipo_combustivel):
        """ Usamos o 'super()' para acessar a calsse superior e passamos no construtor
        os atributos necessários"""
        super().__init__(marca, modelo, qtd_rodas)

        self.tipo_combustivel = tipo_combustivel # Atributo exclusivo do "Carro"

    def ligar_radio(self):
        print("Rádio está ligado!")

      

camaro = Carro(
    marca = 'Chevrolet',
    modelo = "Camaro SS",
    qtd_rodas = 4,
    tipo_combustivel = "Gasolina"
)
camaro.acelerar()
camaro.ligar_radio()
camaro.mudar_direcao("Direita")
camaro.frear()
# Exemplo de Composição
class Motor:
    def __init__(self, tipo):
      self.tipo = tipo

    def ligar(self):
      print(f"motor {self.tipo} ligado")

    def desligar(self):
      print(f"Motor {self.tipo} desligado")

class Carro:
  def __init__(self, modelo, cor, motor: Motor):
    self.modelo = modelo
    self.cor = cor
    self.motor = motor # O carro recebe um objeto da classe Motor

  def ligar(self):
    print(f"O carro {self.modelo} está ligando...")
    self.motor.ligar() # Chama o método motor

  def desligar(self):
    print(f"O carro {self.modelo} está desligando...")
    self.motor.desligar() # Chama o método motor

# Testando a composição
motor_v8 = Motor("V8")
carro = Carro("Fusca", "Azul", motor_v8)

carro.ligar()
carro.desligar()


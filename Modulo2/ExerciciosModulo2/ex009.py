""" 
EXERCÍCIO 1 
Crie uma classe Carro (nome) depois crie uma classe Motor (nome) e por fim crie uma classe
fabricante (nome). Faça a ligação entre Carro e Motor. 
OBS: um fabricante pode fabricar vários
carros.
Exiba na tela o nome do motor e fabricante. 
""" 
class Carro:
  def __init__(self, nome):
    self.nome = nome
    self._motor = None
    self._fabricante = None 

  @property 
  def motor(self):
    return self._motor

  @motor.setter
  def motor(self, valor):
    self._motor = valor 

  @property
  def fabricante(self):
    return self._fabricante

  @fabricante.setter 
  def fabricante(self, valor):
    self._fabricante = valor 

class Motor:
  def __init__(self, nome):
    self.nome = nome

class Fabricante:
  def __init__(self, nome):
    self.nome = nome

fusca = Carro("Fusca")
Volkswagen = Fabricante("Volkswagen")
motor_1_0 = Motor("1.0")
fusca.fabricante = Volkswagen 
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = Volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)
    
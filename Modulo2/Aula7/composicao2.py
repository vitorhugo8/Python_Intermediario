# +1 Exemplo de Composição
class Cliente:
  def __init__(self, nome):
    self.nome = nome
    self.enderecos = []

  def inserir_endereco(self, rua, numero):
    self.enderecos.append(Endereco(rua, numero)) # Quando 'Cliente' deixar de existir, o método que instãncia a classe Endereco também deixa de existir

  def listar_enderecos(self):
    for endereco in self.enderecos:
      print(endereco.rua, endereco.numero)


class Endereco:
  def __init__(self, rua, numero):
    self.rua = rua
    self.numero = numero



cliente1 = Cliente("Roberto")
cliente1.inserir_endereco("Rua Mariz e Barros", 1234)
print(cliente1.nome)
cliente1.listar_enderecos()


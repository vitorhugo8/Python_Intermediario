# Exemplo de Agregação
class Livro:
  def __init__(self, titulo):
    self.titulo = titulo

  def __str__(self):
    return self.titulo

class Biblioteca:
  def __init__(self, nome):
    self.nome = nome
    self.livros = [] # Lista de livros (Agregação)

  def adicionar_livros(self, livro):
    self.livros.append(livro)

  def listar_livros(self):
    print(f"Livros na bilioteca {self.nome}")
    for livro in self.livros:
      print(livro)

# Testando a agregação
livro1 = Livro("Python para Iniciantes")
livro2 = Livro("POO com Python")

biblioteca = Biblioteca("Biblioteca Virtual")
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)

biblioteca.listar_livros()
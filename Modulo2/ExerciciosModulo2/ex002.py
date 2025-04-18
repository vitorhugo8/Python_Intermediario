class Livros:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} está disponível! Pode pegar")
        else:
            print(f"Desculpe, o livro {self.titulo} não está disponível")

    def devolver(self):
        self.disponivel = True
        print(f"Livro {self.titulo}, devolvido com sucesso")

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({self.ano_publicado}) [{status}]"

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_emprestimos = []

    def emprestar_livros(self, livro):
        if len(self.lista_de_emprestimos) < 3 and livro.disponivel:
            livro.emprestar()
            self.lista_de_emprestimos.append(livro)
        elif not livro.disponivel:
            print(f"O livro {livro.titulo} não está disponível")
        else:
            print(f"{self.nome} já atingiu o limite de 3 livros")

    def devolver_livro(self, livro):
        if livro in self.lista_de_emprestimos:
            livro.devolver()
            self.lista_de_emprestimos.remove(livro)
        else:
            print(f"{self.nome} não tem esse livro emprestado")

class UsuarioPremium(Usuario):
    def emprestar_livros(self, livro):
        if len(self.lista_de_emprestimos) < 10 and livro.disponivel:
            livro.emprestar()
            self.lista_de_emprestimos.append(livro)
        elif not livro.disponivel:
            print(f"O livro {livro.titulo} não está disponível")
        else:
            print(f"{self.nome} já atingiu o limite de 10 livros")

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livros(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        print("📚 Livros disponíveis:")
        for livro in self.livros:
            if livro.disponivel:
                print(f"- {livro}")

livro1 = Livros("1984", "George Orwell", 1949)
livro2 = Livros("Dom Casmurro", "Machado de Assis", 1899)
livro3 = Livros("O Hobbit", "J.R.R. Tolkien", 1937)

biblioteca = Biblioteca()
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)
biblioteca.adicionar_livros(livro3)

usuario1 = Usuario("João")
usuario2 = UsuarioPremium("Maria")

biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

biblioteca.listar_livros_disponiveis()

usuario1.emprestar_livros(livro1)
usuario2.emprestar_livros(livro2)
usuario1.emprestar_livros(livro2)

usuario2.devolver_livro(livro2)

biblioteca.listar_livros_disponiveis()

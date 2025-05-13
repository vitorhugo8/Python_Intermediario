"""
Empacotamento e Desempacotamento condicionados. 

Relembrando - Empacotamento ocorre quando múltiplos valores são agrupados em uma única
estrutura de dados, como uma tupla ou uma lista. 

Desempacotamento - Ocorre quando os valores armazenados em uma estrutura de dados 
são extraídos em variáveis individuais.

Kwargs (keyword arguments) - é um recurso que permite passar um número variável de 
argumentos nomeados para uma função. Isso significa que podemos chamar uma função com
diferentes quantidades de parâmetros sem precisar definir cada um individualmente. 

Usamos kwargs quando não sabemos quantos argumentos nomeados serão passados.

É "ativado" com duas estrelas antes do argumento.
"""
# Exemplo de Empacotamento
valores = 1, 2, 3
print(valores)

# Exemplo de Desempacotamento
a, b, c = valores
print(a, b, c)

# Desempacotamento de dicionários utilizando kwargs
def exibir_dados(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

dados = {
    "nome": "Alice",
    "idade": 29,
    "cidade": "Manaus"
}

exibir_dados(**dados) # Desempacota o dicionário
print(10 * "==")


# Exemplo de 'kwargs'
def exibir_informações(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_informações(nome="Alice", idade=25, cidade="São Paulo") # Passando os itens como dicionário para dentro da função que os exibirá na tela

# Exemplo de 'kwargs' 2 
def configurar_nome(nome, **config):
    print(f"Usuário: {nome}")
    for chave, valor in config.items():
        print(f"{chave}: {valor}")

configurar_nome("Carlos", tema="escuro", notificacoes="True", idioma="PT-BR")
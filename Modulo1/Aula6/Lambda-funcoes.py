"""
Criamos uma função que recebe uma expressão lambda por conta de boas práticas de 
programação. A PEP 8 não recomenda a criação de uma expressão lambda diretamente no 
código, sem que ela seja atribuída a uma variável ou passada como argumento para 
outra função.
"""
# Função que recebe outra função como argumento + argumentos variáveis 
def executa(funcao, *args):
    return funcao(*args)

# Função que soma dois numeros 
def soma(x, y):
    return x + y

# Função que retorna outra função que multiplica um numero por um multiplicador (Ex. closure)
# Essa função faz a mesma coisa que a função 'duplica', porém, é mais legível
def cria_mult(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# Cria multiplicador de um número usando Lambda
duplica = executa(
    lambda x: lambda y: y * x, 2
)

print(duplica(2))
print(executa(lambda x, y: x + y, 2, 3))
print(executa(soma, 2, 3))
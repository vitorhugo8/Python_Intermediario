# Função que recebe outra função como argumento e faz a operação de soma de dois numeros
def executa(funcao, *args):
    return funcao(*args)

# Função que soma dois numeros 
def soma(x, y):
    return x + y


def cria_mult(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_mult(2)
print(duplica)


print(executa(lambda x, y: x + y, 2, 3))
print(executa(soma, 2, 3))
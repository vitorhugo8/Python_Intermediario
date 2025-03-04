"""
Crie uma função chamada soma_todos que recebe um número variável 
de argumentos e retorna a soma de todos eles. Em seguida, 
utilize essa função desempacotando uma lista de números.

"""
# Opção 1
def soma_todos(*args):
    soma = sum([*args])
    print(f"Total: {soma}")
 
soma_todos(6, 6)

# Opção 2
def somaTodos(*lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

print(somaTodos(2, 2, 2, 2, 2, 2))

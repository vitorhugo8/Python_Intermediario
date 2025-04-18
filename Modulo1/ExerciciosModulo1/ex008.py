"""
Crie dois conjuntos:
pares = {2, 4, 6, 8, 10}
impares = {1, 3, 5, 7, 9}

Agora escreva um código para:
    1 - Criar um conjunto chamado "todos" que contém a união
    de dois conjuntos.
    2 - Criar um conjunto chamado vazio que contém a interseção dos dois conjuntos.
    3 - Exibir os conjuntos resultantes.

"""
pares = {2, 4, 6, 8, 10}
impares = {1, 3, 5, 7, 9}

todos = pares | impares
print(todos)

vazio = pares & impares
print(vazio)





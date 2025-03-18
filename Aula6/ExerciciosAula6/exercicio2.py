"""
NIVEL INTERMEDIARIO

1 - Dada uma lista de tuplas, use sorted() com uma lambda para ordená-la 
pelo segundo valor de cada tupla.

2 - Crie uma lambda que recebe um número e retorna outra função 
que multiplica qualquer número por ele.

3 - Use filter() e lambda para filtrar os números ímpares de uma lista.

"""
dados = [(1, 3), (4, 1), (2, 2)]
ordenado = sorted(dados, key=lambda x: x[1])
print(ordenado)
print(10 * "==")

multiplicador = lambda m: lambda n: n * m
duplica = multiplicador(2) 
print(duplica(5))
print(10 * "==")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtro = filter(lambda x: x % 2 != 0, numeros)
print(list(filtro))


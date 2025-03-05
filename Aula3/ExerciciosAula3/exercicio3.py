"""
Use a função filter com uma função lambda para 
filtrar os números ímpares de uma lista.
"""

numeros = [7, 8, 9, 10]
filtro = filter(lambda x: x % 2 != 0, numeros)
print(list(filtro))
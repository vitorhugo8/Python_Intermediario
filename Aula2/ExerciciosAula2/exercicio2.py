"""
Dada a lista valores = [10, 20, 30, 40, 50], 
use o operador * para armazenar o primeiro elemento em uma variável chamada primeiro, 
o último em uma variável chamada ultimo, e o restante dos valores em uma 
lista chamada meio. Depois, imprima cada uma dessas variáveis.
"""
lista = [10, 20, 30, 40, 50]
primeiro, *meio, ultimo = lista

print("Primeiro:", primeiro)
print("Meio:", meio)
print("Último:", ultimo)
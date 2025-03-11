"""
Sets - São uma coleção de itens desordeana, parcialmente imutável e que não 
podem conter elementos duplicados. Por ser parcialmente imutável, os sets possuem
permissão de adição e remoção de elementos.

-> Sets são efificientes para remover valores duplicados de iteráveis. 
-> Não tem indices 
-> Não tem ordem
"""
# Removendo valores repetidos da lista 
lista = [1, 2, 3, 4, 4, 4, 4, 5]
set_lista = set(lista)

print(set_lista)

# Métodos úteis em Set:
# ADD
s = set()
s.add(1)
s.update("Olá mundo!")
print(s)

# CLEAR
# s.clear()

# DISCARD
# s.discard("mundo")
# print(s)

# União '|'
n1 = {1, 2, 3, 4}
n2 = {4, 5, 6, 7}
numeros = n1 | n2
print(numeros)

# Interseção '&'
n3 = n1 & n2
print(n3)

n4 = n1 - n2
print(n4)

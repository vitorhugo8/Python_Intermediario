"""
List comprehension é uma forma rápida de criar listas em python
"""

# Manipulando uma lista de forma tradicional 
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {"nome": "Maçã", "preço": 2.90},
    {"nome": "Pera", "preço": 5.90},
    {"nome": "Banana", "preço": 4.90},
]

novos_produtos = [
    {**produto, "preço": produto["preço"] * 1.05}
    for produto in produtos
    
]
print("Aumento dos produtos em 5%\n")
print(*novos_produtos)

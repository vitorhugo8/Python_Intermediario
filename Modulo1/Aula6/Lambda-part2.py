"""
Função Lamda - Como já vimos anteriormente, lambda é uma função anônima, que pode ser
descartada durante a execução do código. 

"""
# Ordenando elementos de uma lista com Lambda
lista0 = [
    # Dicionário
    {"Alimento": "1K Café", "preço": 24.90},
    {"Alimento": "1K de Maçã", "preço": 13.50},
    {"Alimento": "10 pães de forma", "preço": 2.99},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista0, key=lambda item: ["preço"])
l2 = sorted(lista0, key=lambda item: ["Alimento"])

exibir(l1)
exibir(l2)

# Ordenando uma lista com comando nativos do Python
print("==" * 10)
lista = [4, 32, 20, 1, 3, 21, 15, 2]
lista.sort()

print(lista)
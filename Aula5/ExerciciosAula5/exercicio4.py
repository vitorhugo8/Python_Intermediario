"""
Crie uma função que encontra o primeiro duplicado considerando o segundo número
como a duplicação. Retorne a duplicação considerada 
================================================
RESOLUÇÃO:
1. Criar um conjunto vazio chamado numeros vistos, que armazena todos os números que 
já foram encontrados

2. Iterar pela lista, verificando se ela já se encontra no conjunto de números_vistos.

3. Se o número não estiver no conjunto, adicionamos ele, garantindo que só consideramos
o segundo número como duplicação. Por exemplo, se em uma lista tivermos [2, 4, 6, 8, 4]
O primeiro quatro será adicionado a lista, e o segundo será retornado.

"""
def duplicado(lista):
    numeros_vistos = set()

    for numero in lista: # Se o número já estiver no conjunto, é duplicação 
        return numero 
    numeros_vistos.add(numero) # Adiciona o número ao conjunto se ainda não estiver lá

    return -1 # Se não houver duplicatas, retorna -1

teste = [5, 4, 3, 3, 4, 5, 6]
print(duplicado(teste))
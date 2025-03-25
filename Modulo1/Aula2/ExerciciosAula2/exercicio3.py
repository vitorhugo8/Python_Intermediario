"""
1 - Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.

2 - Crie uma função que fala se um número é par ou ímpar. Se for par, o programa
deve retornar True, se não, deve retornar False.
"""

# Exercicio 1
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero # Ou total = total * numero
    print("O produto da multiplicação de todos os itens da lista é: ",total)

multiplica(6, 2, 2)

# Exercicio 2
def par_impar(num):
    return num % 2 == 0

print(par_impar(8))
print(par_impar(5))

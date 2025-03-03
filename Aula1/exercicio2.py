"""
Objetivo: Criar uma função que retorne 
os primeiros N números da sequência de Fibonacci.

Dica: Utilizar um algoritimo de recursão.

"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
   
for i in range(10):
    print(fibonacci(i), end= " ")
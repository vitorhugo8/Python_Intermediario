"""
Objetivo: Criar uma função para realizar 
operações matemáticas básicas (soma, subtração, multiplicação, divisão).

Crie uma função para cada operação.
Crie uma função principal que receba dois números e o tipo de operação, 
e chame a função correspondente.

"""
def soma(a, b):
        print(f"A soma entre {a} e {b} é igual a {a + b}")

def sub(a, b):
        print(f"A subtração de {a} por {b} é igual a {a - b}")

def mult(a, b):
        print(f"A multiplicação de {a} por {b} {a * b}")

def div(a, b):
        print(f"A divisão de {a} por {b} é {a / b}")


a = int(input("Que número você deseja adicionar primeiro?: "))
b = int(input("Qual o segundo número?: "))
decisao = int(input("Que operação você deseja realizar? \n1) Soma \n2) Subtração \n3) Multiplicação \n4) Divisão \n"))

if decisao == 1:
        soma(a, b)
elif decisao == 2:
        sub(a, b)
elif decisao == 3:
        mult(a, b)
elif decisao == 4:
        div(a, b)
else:
        print("Me desculpe, eu não reconheci a sua entrada, tente de novo")
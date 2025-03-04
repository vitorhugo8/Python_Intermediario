"""
Utilizando loops para fazer contagem de números em ordem. 
O parâmetro '*args' recebe dados ilimitados quando chamado pela função. 
Como vimos anteriormente, o operador ' * ' recebe dados ilimitados. 

"""
def soma(*args):
    total = 0 # Acumulador 
    for numero in args:
        print("Somando os valores: ",total, numero)
        total = total + numero
        print("Total: ", total)
    print(total)

soma(1, 2, 3, 4, 5, 6)


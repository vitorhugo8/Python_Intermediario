"""
Crie uma função de alta ordem chamada aplicar_funcao que recebe uma função e um 
valor como argumento e retorna o resultado da função aplicada ao valor.

"""
def aplicar_funcao(funcao, val):
    return funcao(val)

dobro = lambda x: x * 2
print(aplicar_funcao(dobro, 5))
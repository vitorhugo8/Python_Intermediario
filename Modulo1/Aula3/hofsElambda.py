"""
High Order functions (HOF's) / Funções de Primeira classe.
Referem-se a funções que retornam outras funções como resultado ou 
recebem funções como argumento.

First-Class Functions / Funções de Primeira Classe - Trata-se de funções que 
podem ser tratadas como objetos. Isso significa que podem ser atribuidas a variáveis, 
passadas como parâmetros para outras funções, e incorporadas em estrutras de dados. 

Lambda - É uma função anônima, uma pequena função sem nome, que utiliza a 
palavra lambda como palvra-chave. É utilizada quando deseja-se criar uma 
função descartável no código

Built-in - São funções que já estão integradas 
na linguagem e podem ser usadas imediatamente
"""
# Exemplo de HOF 1
def nome_user(nome):
    return f"{nome}"

def saudacao(funcao):
    return f"Bom dia {funcao}"

r = nome_user("vitor hugo")
r1 = saudacao(r) 
print(r1)  


# Exemplo de uso da Lambda 
quadrado = lambda x: x ** 2
resultado = quadrado(4)
print(resultado)

# Exemplo de HOF 2
def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
raiz_quadrada = list(map(potencia, numeros)) 
# A função map é built-in e aplica uma função a cada elemento de uma estrutura de dados iterável
print(raiz_quadrada)

"""
args - Argumentos não nomeados.
Desempacotamento - refere-se a uma técnica de programação que nos permite 
atribuir elementos de uma sequência (lista, tupla ou string) a variáveis
individuais de forma simples.

O Operador ' * ' é utilizado para agrupar valores restantes em uma lista. 
Útil quando você não sabe ao certo quantos elemntos a variável irá receber. 

Desempacotar sequências em Python é uma técnica essencial 
que pode simplificar muito o seu código. Seja você um desenvolvedor 
intermediário ou avançado, entender e aplicar o desempacotamento de 
sequências pode tornar seu trabalho mais eficiente e seu código mais limpo. 
"""
# Exemplo de desempacotamento com tupla 
print(30*"==")
tupla = (10, 20, 30)
a, b, c = tupla 

print(a)
print(b)
print(c)

# Exemplo de desempacotamento com lista 
print(30*"==")
lista = [5, 10, 15, 20]
p1, p2, p3, p4 = lista 

print(p1)
print(p2)
print(p3)
print(p4)

# Exemplo de desempacotamento com string
print(30*"==")
string = "Python"
a, b, c, d, e, f = string

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Exemplo de uso do operador *
print(30*"==")
numeros = [1, 2, 3, 4, 5]
primeiro, segundo, *resto = numeros 

print(primeiro)
print(segundo)
print(resto)

"""
NIVEL BÁSICO

1 - Crie uma função que receba dois números e retorne a soma deles.

2 - Crie uma função lambda que receba um número e retorne True se ele 
for par e False caso contrário.

3 - Crie uma lambda que receba uma string e retorne o primeiro caractere.

"""
soma = lambda x, y: x + y
print(soma(2, 3))
print(10 * "==")

par_impar = lambda x: x % 2 == 0
print(par_impar(5))
print(10 * "==")

primeiro_caractere = lambda s: s[0]
print(primeiro_caractere("House"))


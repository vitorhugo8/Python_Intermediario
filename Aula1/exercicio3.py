"""
Crie uma função que calcule a área de um círculo.
A fórmula é área = pi * raio^2

"""
from math import pi, trunc
raio = float(input("Qual é o raio do círculo que você deseja calcular: "))

def circulo(raio):
    area = pi * raio**2
    return trunc(area)

print(circulo(raio))

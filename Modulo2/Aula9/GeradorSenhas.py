"""
Desafio: criar um gerador de códigos de autenticação de 6 digitos, usados em autenticação
de dois fatores (2FA)

Regras: 
Gera um número aleatório de 6 dígitos. 
Usa uma closure para definir a validade do código. 
Adiciona uma função lambda para fromatar a saída do código. 
"""
import random
def gerar_senha():
    lista = [1, 2, 3, 4, 5, 6]
    senha = random.shuffle(lista)
    print(senha)

gerar_senha()
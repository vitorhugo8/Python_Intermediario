"""
Introdução as funções (def) em Python.
Funções são trechos de código usados para replicar 
determinada ação ao longo do código.

Elas podem (ou não) receber parâmetros (argumentos)
e retornar um valor específico. Por padrão, funções Python retornam None (nada).
"""
def saudacao(nome= "indefinido "):
    print(f"Seja bem vindo, {nome}")

saudacao("Jorge")
saudacao()


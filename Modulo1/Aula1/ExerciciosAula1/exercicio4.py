"""
Crie uma função que  converta a temperatura de Celsius para Fahrenheit. 
A fórmula é Fahrenheit = (Celsius * 9/5) + 32.
"""
temp = int(input("Escreva a temperatura em Celsius: "))

def conversaoF(temp):
    Farenheit = (temp * (9/5)) + 32
    print(f"{Farenheit} Graus Farenheit")

conversaoF(temp)
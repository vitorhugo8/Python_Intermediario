"""
Peça ao usuário para digitar duas frases. Depois, crie dois conjuntos contendo as 
palavras únicas de cada frase e mostre quais palavras aparecem em ambas as frases.

"""
palavra1 = str(input("Digite uma frase: "))
palavra2 = str(input("Digite mais uma frase: "))

set_p1 = set(palavra1)
set_p2 = set(palavra2)

frase = set_p1 | set_p2
print(frase)
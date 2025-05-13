"""
Exemplo de uso dos Sets. 

"""
letras = set()
while True:
    letra = input("Digite: ").lower()
    letras.add(letra)

    if "l" in letras:
        print("Parabéns! Essa é a letra secreta")
        break

print(f"Número de tentativas: {letras}")
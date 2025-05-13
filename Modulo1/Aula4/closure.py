"""
Closure - É um objeto de função que lembra dos valores nos escopos envolventes.
"""
def saudacao(saudacao, nome):
    def saudar():
        return f"{saudacao}, {nome}"
    return saudar()


s1 = saudacao("Bom dia", "Maria")
print(s1)


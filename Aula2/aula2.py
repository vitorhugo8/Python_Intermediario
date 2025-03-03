"""
Escopo significa o local onde aquele código pode atingir 
Existe o escopo global e local.
O escopo global é onde todo o código é alcançavel, ou seja, 
toda variável denominada 'global' pode ser acessada em todo o código. 
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

Dica: Sempre fazer a refatoração de um código. Ele sempre pode melhorar.

"""
x = 1 # Variável Global 

def escopo():
    print(x)
    numero_legal = x + 5 # Variável Local
    print(numero_legal)

escopo()


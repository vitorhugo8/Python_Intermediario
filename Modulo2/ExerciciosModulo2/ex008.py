"""
Desafio: criar uma classe ContaBancaria que simula uma conta simples de banco,
utilizando o decorator @property para controle de acesso e validação de dados.

Dica: Separar dados (numéricos) de mensagens (strings) nos getters deixa o código 
mais reutilizável e limpo. Deixar a formatação para o momento em que for exibir ou registrar
informações. 
"""

class ContaBancaria:
    def __init__(self, saldo, limite):
        self._saldo = saldo
        self._limite = limite

    # Propriedade saldo
    @property
    def saldo_atual(self):
        return self._saldo

    @saldo_atual.setter
    def saldo_atual(self, novo_saldo):
        if novo_saldo > 0 and novo_saldo <= self._limite:
            self._saldo = novo_saldo
        elif novo_saldo > self._limite:
            print("❌ Seu limite não permite essa alteração no saldo.")
        else:
            print("❌ Saldo inválido.")

    # Propriedade limite
    @property
    def limite_atual(self):
        return self._limite

    @limite_atual.setter
    def limite_atual(self, novo_limite):
        if novo_limite >= 0:
            self._limite = novo_limite
        else:
            raise ValueError("❌ O limite não pode ser negativo.")

    # Métodos bancários
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"✅ Depósito realizado: R${valor}")
        else:
            print("❌ Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= (self._saldo + self._limite):
            self._saldo -= valor
            print(f"✅ Saque realizado: R${valor}")
        else:
            print(f"❌ Limite insuficiente para sacar R${valor}.")

    def extrato(self):
        print("📄 Extrato da Conta:")
        print(f"   Saldo:  R${self._saldo}")
        print(f"   Limite: R${self._limite}")

c1 = ContaBancaria(saldo=2000, limite=8000)
c1.depositar(200)
c1.sacar(1800)
c1.limite_atual = 50000
c1.saldo_atual = 6000
c1.extrato()
import re

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """
        Verifica se o CPF está no formato XXX.XXX.XXX-XX
        Exemplo válido: 123.456.789-09
        """
        padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        return bool(re.match(padrao, cpf))

    @classmethod
    def criar_pessoa(cls, nome: str, cpf: str):
        """
        Cria uma instância de Pessoa se o CPF for válido.
        Caso contrário, levanta ValueError.
        """
        if cls.validar_cpf(cpf):
            return cls(nome, cpf)
        else:
            raise ValueError("CPF inválido. Formato esperado: XXX.XXX.XXX-XX")

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}"

# Testando a classe
pessoa1 = Pessoa.criar_pessoa("João", "123.456.789-09")
print(pessoa1)
print(pessoa1.validar_cpf("123.456.789-09")) 

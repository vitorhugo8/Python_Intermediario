import json
caminho = "aula3.json" # caminho para onde os dados serão enviados

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

p1 = Pessoa("João", 13)
p2 = Pessoa("Mariana", 14)
p3 = Pessoa("Kiara", 15)
bd = [vars(p1), p2.__dict__, vars(p3)] # Convertendo os dados para dicionário

with open(caminho, "w") as f: # Abrimos o 'caminho' no modo de escrita e colocamos nossos dados já tratados
    json.dump(bd, f, ensure_ascii=False, indent=2)

"""
JSON (JavaScript Object Notation) é um formato de texto que permite aramazenar e trocar dados
entre sistemas. É um formato leve e legível por humanos. O JSON é muito utilizado em API's e
aplicações web para transferência de dados entre cliente e servidor.

JSON é um formato aberto e independente de linguagem de programação. É derivado do JavaScript, 
mas não suporta funções como uma linguagem de programação de verdade. 

CURIOSIDADE -- O package.json é um arquivo JSON central em projetos de desenvolvimento 
de software em JavaScript e Node.js para gerenciar as dependências, informações sobre o projeto, 
scripts de execução e metadados do projeto.
"""
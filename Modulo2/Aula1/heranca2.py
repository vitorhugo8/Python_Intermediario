""" 
Criando um sistema de RPG utilizando o conceito de Herança.

Os personagens tem caracterísicas em comum como: nome, defesa, pontos de vida e
pontos de experiência. A ideia do código é que a classe personagem sirva como base para 
criar personagens de diferentes níveis de poder e experiência"""

class Personagem:
    def __init__(self, nome, defesa, pv, pex):
        self.nome = nome
        self.defesa = defesa
        self.pv = pv
        self.pex = pex

        self.poderes_por_nivel = [
        (50, "Você não tem poderes, pois seu corpo atingiu o patamar dos deuses"),
        (30, "O seu poder é ficar invisível"),
        (20, "O seu poder é super-força"),
        (10, "Você é capaz de manipular todo tipo de arma branca que quiser"),
        (0, "Você não possui experiência suficiente para manifestar algum poder"),
    ]

    def poderes(self):
        for nivel, poder in self.poderes_por_nivel:
            if self.pex >= nivel:
                print(poder)
                return

# Criando mais um personagem 
class Druida(Personagem):
    def __init__(self, nome, defesa, pv, pex, poder_druida):
        super().__init__(nome, defesa, pv, pex)

        self.poder_druida = poder_druida

    def feitico(self):
        print(f"O inimigo foi atacado pela sua {self.poder_druida}!")

lucas = Druida("luquinas de SP", defesa=50, pv=120, pex=30, poder_druida="Bola de fogo")
lucas.poderes()
lucas.feitico()

class Bardo(Personagem):
    def __init__(self, nome, defesa, pv, pex, poder_bardo):
        super().__init__(nome, defesa, pv, pex)

        self.poder_bardo = poder_bardo
    
    def ataque_bardo(self):
        print(f"O inimigo foi atacado pelo seu {self.poder_bardo}")

marcos = Bardo("Antônio", defesa=40, pv=100, pex=50, poder_bardo="Golpe pesado")
marcos.ataque_bardo()
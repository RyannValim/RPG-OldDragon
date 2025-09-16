from model.bases.classe_base import Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__(
            nome="Guerreiro",
            dado_de_vida=10,
            ba_inicial=1,
            jp_inicial=5,
            prioridade_atributos=["FOR", "CON", "DES", "SAB", "CAR", "INT"] # NOVA LISTA
        )

    def aplicar_bonus_de_classe(self, personagem):
        super().aplicar_bonus_de_classe(personagem)
        personagem.proficiencias.append("Armas: Todas.")
        personagem.proficiencias.append("Armaduras: Todas.")
        personagem.habilidades.append("Aparar: Pode sacrificar escudo ou arma para absorver todo o dano de um ataque.")
        personagem.habilidades.append("Maestria em Arma: No 1º nível, escolhe uma arma para ter +1 de bônus no dano.")
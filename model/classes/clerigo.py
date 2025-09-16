from model.bases.classe_base import Classe

class Clerigo(Classe):
    def __init__(self):
        super().__init__(
            nome="Clérigo",
            dado_de_vida=8,
            ba_inicial=1,
            jp_inicial=5,
            prioridade_atributos=["SAB", "CON", "FOR", "CAR", "DES", "INT"]
        )

    def aplicar_bonus_de_classe(self, personagem):
        super().aplicar_bonus_de_classe(personagem)
        personagem.proficiencias.append("Armas: Apenas armas de impacto (maças, martelos, etc.).")
        personagem.proficiencias.append("Armaduras: Todas.")
        personagem.habilidades.append("Magias Divinas: Capaz de lançar magias divinas a partir do 1º nível.")
        personagem.habilidades.append("Afastar Mortos-Vivos: Pode invocar poder divino para afugentar mortos-vivos.")
        personagem.habilidades.append("Cura Milagrosa: Pode trocar uma magia memorizada por uma de 'Curar Ferimentos'.")
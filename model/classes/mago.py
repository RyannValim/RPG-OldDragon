from model.bases.classe_base import Classe

class Mago(Classe):
    def __init__(self):
        super().__init__(
            nome="Mago",
            dado_de_vida=4,
            ba_inicial=0,
            jp_inicial=5,
            prioridade_atributos=["INT", "DES", "CON", "SAB", "CAR", "FOR"]
        )

    def aplicar_bonus_de_classe(self, personagem):
        super().aplicar_bonus_de_classe(personagem)
        personagem.proficiencias.append("Armas: Apenas armas pequenas (adagas, cajados).")
        personagem.proficiencias.append("Armaduras: Nenhuma.")
        personagem.habilidades.append("Magias Arcanas: Capaz de lançar magias arcanas a partir do 1º nível.")
        personagem.habilidades.append("Grimório: Começa com um grimório contendo 4 magias de 1º círculo.")
        personagem.habilidades.append("Ler Magias: Pode decifrar inscrições mágicas.")
        personagem.habilidades.append("Detectar Magias: Pode perceber a presença de magia.")
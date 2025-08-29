class Classe:
    def __init__(self, nome, dado_de_vida, ba_inicial, jp_inicial):
        self.nome = nome
        self.dado_de_vida = dado_de_vida
        self.ba_inicial = ba_inicial # base de ataque
        self.jp_inicial = jp_inicial # jodada de proteção

    def aplicar_bonus_de_classe(self, personagem):
        personagem.pontos_de_vida = self.dado_de_vida + personagem.atributos['CON']['mod']
        personagem.base_de_ataque = self.ba_inicial
        personagem.jogada_de_protecao = self.jp_inicial

class Guerreiro(Classe):
    def __init__(self):
        super().__init__(
            nome="Guerreiro",
            dado_de_vida=10,
            ba_inicial=1,
            jp_inicial=5
        )

    def aplicar_bonus_de_classe(self, personagem):
        super().aplicar_bonus_de_classe(personagem)
        personagem.proficiencias.append("Armas: Todas.")
        personagem.proficiencias.append("Armaduras: Todas.")
        personagem.habilidades.append("Aparar: Pode sacrificar escudo ou arma para absorver todo o dano de um ataque.")
        personagem.habilidades.append("Maestria em Arma: No 1º nível, escolhe uma arma para ter +1 de bônus no dano.")

class Clerigo(Classe):
    def __init__(self):
        super().__init__(
            nome="Clérigo",
            dado_de_vida=8,
            ba_inicial=1,
            jp_inicial=5
        )

    def aplicar_bonus_de_classe(self, personagem):
        super().aplicar_bonus_de_classe(personagem)
        personagem.proficiencias.append("Armas: Apenas armas de impacto (maças, martelos, etc.).")
        personagem.proficiencias.append("Armaduras: Todas.")
        personagem.habilidades.append("Magias Divinas: Capaz de lançar magias divinas a partir do 1º nível.")
        personagem.habilidades.append("Afastar Mortos-Vivos: Pode invocar poder divino para afugentar mortos-vivos.")
        personagem.habilidades.append("Cura Milagrosa: Pode trocar uma magia memorizada por uma de 'Curar Ferimentos'.")

class Mago(Classe):
    def __init__(self):
        super().__init__(
            nome="Mago",
            dado_de_vida=4,
            ba_inicial=0,
            jp_inicial=5
        )

    def aplicar_bonus_de_classe(self, personagem):
        super().aplicar_bonus_de_classe(personagem)
        personagem.proficiencias.append("Armas: Apenas armas pequenas (adagas, cajados).")
        personagem.proficiencias.append("Armaduras: Nenhuma.")
        personagem.habilidades.append("Magias Arcanas: Capaz de lançar magias arcanas a partir do 1º nível.")
        personagem.habilidades.append("Grimório: Começa com um grimório contendo 4 magias de 1º círculo.")
        personagem.habilidades.append("Ler Magias: Pode decifrar inscrições mágicas.")
        personagem.habilidades.append("Detectar Magias: Pode perceber a presença de magia.")
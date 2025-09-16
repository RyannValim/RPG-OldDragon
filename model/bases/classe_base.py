class Classe:
    def __init__(self, nome, dado_de_vida, ba_inicial, jp_inicial, prioridade_atributos):
        self.nome = nome
        self.dado_de_vida = dado_de_vida
        self.ba_inicial = ba_inicial
        self.jp_inicial = jp_inicial
        self.prioridade_atributos = prioridade_atributos # NOVA LINHA

    def aplicar_bonus_de_classe(self, personagem):
        # Garante que o modificador de CON seja pelo menos 1 nos PV iniciais
        mod_con_pv = personagem.atributos['CON']['mod'] if personagem.atributos['CON']['mod'] > 0 else 0
        personagem.pontos_de_vida = self.dado_de_vida + mod_con_pv
        personagem.base_de_ataque = self.ba_inicial
        personagem.jogada_de_protecao = self.jp_inicial
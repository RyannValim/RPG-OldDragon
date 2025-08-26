class Raca:
    def __init__(self, nome, movimento, infravisao, alinhamento_tipico):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento_tipico = alinhamento_tipico

    def aplicar_habilidades_raciais(self, personagem):
        personagem.movimento = self.movimento
        personagem.infravisao = self.infravisao
        personagem.notas.append(f"Alinhamento Típico de {self.nome}: {self.alinhamento_tipico}")

class Humano(Raca):
    def __init__(self):
        super().__init__(
            nome="Humano",
            movimento=9,
            infravisao="Não possui",
            alinhamento_tipico="Qualquer"
        )

    def aplicar_habilidades_raciais(self, personagem):
        super().aplicar_habilidades_raciais(personagem)
        personagem.habilidades.append("Aprendizado: Recebe 10% de bônus sobre toda experiência (XP).")
        personagem.habilidades.append("Adaptabilidade: Recebe +1 em uma única Jogada de Proteção (JP) à sua escolha.")

class Elfo(Raca):
    def __init__(self):
        super().__init__(
            nome="Elfo",
            movimento=9,
            infravisao="18 metros",
            alinhamento_tipico="Tende à Neutralidade"
        )

    def aplicar_habilidades_raciais(self, personagem):
        super().aplicar_habilidades_raciais(personagem)
        personagem.habilidades.append("Percepção Natural: Detecta portas secretas com 1 em 1d6 (1-2 se procurando).")
        personagem.habilidades.append("Graciosos: Bônus de +1 em testes de JPD (Jogada de Proteção de Destreza).")
        personagem.habilidades.append("Arma Racial: Bônus de +1 nos danos com arcos.")
        personagem.habilidades.append("Imunidades: Imune a sono mágico e paralisia de Ghoul.")

class Anao(Raca):
    def __init__(self):
        super().__init__(
            nome="Anão",
            movimento=6,
            infravisao="18 metros",
            alinhamento_tipico="Tende à Ordem"
        )

    def aplicar_habilidades_raciais(self, personagem):
        super().aplicar_habilidades_raciais(personagem)
        personagem.habilidades.append("Mineradores: Detecta anomalias em pedras com 1 em 1d6 (1-2 se procurando).")
        personagem.habilidades.append("Vigoroso: Bônus de +1 em testes de JPC (Jogada de Proteção de Constituição).")
        personagem.habilidades.append("Inimigos: Ataques contra orcs, ogros e hobgoblins são considerados fáceis.")
        personagem.restricoes.append("Armas Grandes: Não pode usar armas grandes (a menos que sejam de forja anã).")
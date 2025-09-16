from model.bases.raca_base import Raca

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
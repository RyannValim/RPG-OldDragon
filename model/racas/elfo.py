from model.bases.raca_base import Raca

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
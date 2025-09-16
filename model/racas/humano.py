from model.bases.raca_base import Raca

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
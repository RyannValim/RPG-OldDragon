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
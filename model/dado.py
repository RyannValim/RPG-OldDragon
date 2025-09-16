import random

class Dado:
    @staticmethod
    def rolar(quantidade, lados):
        return sum(random.randint(1, lados) for _ in range(quantidade))

    @staticmethod
    def rolar_com_descarte(quantidade, lados, descartar):
        rolagens = [random.randint(1, lados) for _ in range(quantidade)]
        rolagens.sort(reverse=True)
        return sum(rolagens[:quantidade - descartar])
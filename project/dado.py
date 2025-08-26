import random

class Dado:
    """Classe utilitária para lidar com rolagens de dados."""

    @staticmethod
    def rolar(quantidade, lados):
        """Rola uma 'quantidade' de dados com 'lados'."""
        return sum(random.randint(1, lados) for _ in range(quantidade))

    @staticmethod
    def rolar_com_descarte(quantidade, lados, descartar):
        """Rola uma 'quantidade' de dados e descarta os 'descartar' menores."""
        rolagens = [random.randint(1, lados) for _ in range(quantidade)]
        rolagens.sort(reverse=True)
        return sum(rolagens[:quantidade - descartar])
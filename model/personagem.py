# Em model/personagem.py
from model.dado import Dado

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        self.raca = None
        self.classe = None
        
        self.atributos = {
            "FOR": {"valor": 0, "mod": 0}, "DES": {"valor": 0, "mod": 0},
            "CON": {"valor": 0, "mod": 0}, "INT": {"valor": 0, "mod": 0},
            "SAB": {"valor": 0, "mod": 0}, "CAR": {"valor": 0, "mod": 0}
        }
        
        self.pontos_de_vida = 0
        self.movimento = 0
        self.infravisao = ""
        self.base_de_ataque = 0
        self.jogada_de_protecao = 0
        
        self.habilidades = []
        self.proficiencias = []
        self.restricoes = []
        self.notas = []

    def _calcular_modificador(self, valor):
        return (valor - 10) // 2

    # MÉTODO ATUALIZADO
    def definir_atributos(self, estilo, classe_personagem):
        if estilo == 1:
            # Estilo Clássico (não precisa de alteração)
            ordem_attr = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]
            for attr in ordem_attr:
                valor = Dado.rolar(3, 6)
                self.atributos[attr]['valor'] = valor
                self.atributos[attr]['mod'] = self._calcular_modificador(valor)
        
        elif estilo in [2, 3]:
            # Estilos Aventureiro e Heróico (LÓGICA NOVA E AUTOMATIZADA)
            rolagens = []
            if estilo == 2: # Aventureiro
                for _ in range(6):
                    rolagens.append(Dado.rolar(3, 6))
            else: # Heróico
                for _ in range(6):
                    rolagens.append(Dado.rolar_com_descarte(4, 6, 1))
            
            # Ordena os valores do maior para o menor
            rolagens.sort(reverse=True)
            
            # Pega a lista de prioridades da classe do personagem
            prioridades = classe_personagem.prioridade_atributos
            
            # Distribui os melhores valores nos melhores atributos
            for attr, valor in zip(prioridades, rolagens):
                self.atributos[attr]['valor'] = valor
                self.atributos[attr]['mod'] = self._calcular_modificador(valor)

    def exibir_ficha(self):
        # Este método não é mais usado na versão web, mas podemos manter por enquanto
        pass
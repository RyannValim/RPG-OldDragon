import random

class Personagem:
    """
    Representa um personagem com seus atributos e métodos para
    gerar os valores de acordo com diferentes estilos de rolagem.
    """
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0

    def _rolar_dados_classico_aventureiro(self):
        """
        Método auxiliar para rolar 3d6.
        """
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        dado3 = random.randint(1, 6)
        return dado1 + dado2 + dado3

    def _rolar_dados_heroico(self):
        """
        Método auxiliar para rolar 4d6 e eliminar o d6 mais baixo.
        """
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.sort(reverse=True) # Ordena do maior para o menor
        return sum(dados[:3]) # Soma os 3 maiores dados

    def estilo_classico(self):
        """
        Distribui os atributos do personagem usando o estilo clássico.
        As rolagens são atribuídas em ordem fixa.
        """
        self.forca = self._rolar_dados_classico_aventureiro()
        self.destreza = self._rolar_dados_classico_aventureiro()
        self.constituicao = self._rolar_dados_classico_aventureiro()
        self.inteligencia = self._rolar_dados_classico_aventureiro()
        self.sabedoria = self._rolar_dados_classico_aventureiro()
        self.carisma = self._rolar_dados_classico_aventureiro()

    def estilo_aventureiro(self):
        """
        Distribui os atributos do personagem usando o estilo aventureiro.
        As rolagens são atribuídas em ordem fixa.
        """
        # A descrição do livro de regras diz que o estilo aventureiro é igual ao clássico.
        # Mas vamos manter o método separado para clareza e caso as regras mudem.
        self.estilo_classico()

    def estilo_heroico(self):
        """
        Distribui os atributos do personagem usando o estilo heróico.
        O jogador pode escolher para qual atributo cada rolagem vai.
        """
        rolagens = []
        print("\nPara o Estilo Heróico, você fará 6 rolagens e depois distribuirá os resultados.")
        for i in range(6):
            rolagem = self._rolar_dados_heroico()
            rolagens.append(rolagem)
            print(f"Rolagem {i+1}: {rolagem}")

        print("\nAgora, distribua os seguintes valores para os seus atributos:")
        print(rolagens)
        
        atributos_a_definir = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
        
        for atributo in atributos_a_definir:
            while True:
                try:
                    print(f"\nValores restantes para atribuir: {rolagens}")
                    valor = int(input(f"Qual valor você quer atribuir a {atributo.capitalize()}? "))
                    if valor in rolagens:
                        setattr(self, atributo, valor)
                        rolagens.remove(valor)
                        break
                    else:
                        print(f"Valor inválido. Escolha um dos valores restantes: {rolagens}")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")

    def __str__(self):
        """
        Método especial para exibir o personagem de forma formatada.
        """
        return f'---------- Personagem: {self.nome} ----------\nForca="{self.forca}"\nDestreza="{self.destreza}"\nConstituicao="{self.constituicao}"\nInteligencia="{self.inteligencia}"\nSabedoria="{self.sabedoria}"\nCarisma="{self.carisma}"'
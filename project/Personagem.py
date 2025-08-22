import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0

    def _rolagem_classica_aventureira(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        dado3 = random.randint(1, 6)
        return dado1 + dado2 + dado3

    def _rolagem_heroica(self):
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.sort(reverse=True)
        return sum(dados[:3])

    def _distribuir_pontos_livremente(self, rolagens):
        print("\nAgora, distribua os seguintes valores para os seus atributos:")
        print(rolagens)
        
        rolagens_disponiveis = rolagens.copy()
        
        atributos_a_definir = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
        atributos_definidos = []

        while len(atributos_definidos) < len(atributos_a_definir):
            print(f"\nValores restantes para atribuir: {rolagens_disponiveis}")
            
            print("Atributos restantes: ", end="")
            primeiro_atributo = True
            for atributo in atributos_a_definir:
                if atributo not in atributos_definidos:
                    if not primeiro_atributo:
                        print(" | ", end="")
                    print(f"{atributo.capitalize()}", end="")
                    primeiro_atributo = False
            print()
            
            try: 
                valor = int(input("Qual valor você quer usar? "))
                
                if valor not in rolagens_disponiveis:
                    print(f"Valor inválido. Escolha um dos valores restantes: {rolagens_disponiveis}")
                    continue

                print("Escolha o atributo para o qual o valor será atribuído:")
                print("1. Força | 2. Destreza | 3. Constituição | 4. Inteligência | 5. Sabedoria | 6. Carisma")
                escolha_atributo = int(input("Sua escolha: "))
                
                atributo_selecionado = ""
                if escolha_atributo == 1:
                    atributo_selecionado = "forca"
                elif escolha_atributo == 2:
                    atributo_selecionado = "destreza"
                elif escolha_atributo == 3:
                    atributo_selecionado = "constituicao"
                elif escolha_atributo == 4:
                    atributo_selecionado = "inteligencia"
                elif escolha_atributo == 5:
                    atributo_selecionado = "sabedoria"
                elif escolha_atributo == 6:
                    atributo_selecionado = "carisma"
                else:
                    print("Escolha de atributo inválida. Tente novamente.")
                    continue
                
                if atributo_selecionado in atributos_definidos:
                    print(f"O atributo {atributo_selecionado.capitalize()} já foi definido. Escolha outro.")
                    continue

                if atributo_selecionado == "forca":
                    self.forca = valor
                elif atributo_selecionado == "destreza":
                    self.destreza = valor
                elif atributo_selecionado == "constituicao":
                    self.constituicao = valor
                elif atributo_selecionado == "inteligencia":
                    self.inteligencia = valor
                elif atributo_selecionado == "sabedoria":
                    self.sabedoria = valor
                elif atributo_selecionado == "carisma":
                    self.carisma = valor
                
                atributos_definidos.append(atributo_selecionado)
                rolagens_disponiveis.remove(valor)
                
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    def estilo_classico(self):
        self.forca = self._rolagem_classica_aventureira()
        self.destreza = self._rolagem_classica_aventureira()
        self.constituicao = self._rolagem_classica_aventureira()
        self.inteligencia = self._rolagem_classica_aventureira()
        self.sabedoria = self._rolagem_classica_aventureira()
        self.carisma = self._rolagem_classica_aventureira()

    def estilo_aventureiro(self):
        rolagens = []
        print("\nPara o Estilo Aventureiro, você fará 6 rolagens (3d6) e depois distribuirá os resultados.")
        for i in range(6):
            rolagem = self._rolagem_classica_aventureira()
            rolagens.append(rolagem)
            print(f"Rolagem {i+1}: {rolagem}")
        
        self._distribuir_pontos_livremente(rolagens)

    def estilo_heroico(self):
        rolagens = []
        print("\nPara o Estilo Heróico, você fará 6 rolagens (4d6, descartando o menor) e depois distribuirá os resultados.")
        for i in range(6):
            rolagem = self._rolagem_heroica()
            rolagens.append(rolagem)
            print(f"Rolagem {i+1}: {rolagem}")

        self._distribuir_pontos_livremente(rolagens)

    def __str__(self):
        return f'---------- Personagem: {self.nome} ----------\nForca="{self.forca}"\nDestreza="{self.destreza}"\nConstituicao="{self.constituicao}"\nInteligencia="{self.inteligencia}"\nSabedoria="{self.sabedoria}"\nCarisma="{self.carisma}"'
from dado import Dado

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
        if valor <= 3: return -3
        if valor <= 5: return -2
        if valor <= 8: return -1
        if valor <= 12: return 0
        if valor <= 14: return 1
        if valor <= 16: return 2
        if valor <= 18: return 3
        return 4

    def definir_atributos(self, estilo):
        if estilo == 1:
            print("\nRolando atributos no Estilo Clássico (3d6, sem distribuição)...")
            ordem_attr = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]
            for attr in ordem_attr:
                valor = Dado.rolar(3, 6)
                self.atributos[attr]['valor'] = valor
                self.atributos[attr]['mod'] = self._calcular_modificador(valor)
                print(f"  {attr}: {valor}")
        
        elif estilo in [2, 3]:
            rolagens = []
            if estilo == 2:
                print("\nRolando 6 valores para o Estilo Aventureiro (3d6, com distribuição)...")
                for _ in range(6):
                    rolagens.append(Dado.rolar(3, 6))
            else:
                print("\nRolando 6 valores para o Estilo Heróico (4d6, descartando o menor e com distribuição)...")
                for _ in range(6):
                    rolagens.append(Dado.rolar_com_descarte(4, 6, 1))
            
            print(f"Valores rolados: {rolagens}")
            print("Agora, distribua esses valores entre os atributos.")
            
            rolagens_disponiveis = rolagens.copy()
            attrs_a_definir = list(self.atributos.keys())

            for attr in attrs_a_definir:
                while True:
                    try:
                        print(f"\nValores disponíveis: {rolagens_disponiveis}")
                        valor_escolhido = int(input(f"Escolha um valor para {attr}: "))
                        if valor_escolhido in rolagens_disponiveis:
                            self.atributos[attr]['valor'] = valor_escolhido
                            self.atributos[attr]['mod'] = self._calcular_modificador(valor_escolhido)
                            rolagens_disponiveis.remove(valor_escolhido)
                            break
                        else:
                            print("Valor inválido ou já utilizado. Tente novamente.")
                    except ValueError:
                        print("Erro: Você precisa inserir um número!")

    def exibir_ficha(self):
        print("\n" + "=-"*40 + "=")
        print(f"FICHA DE PERSONAGEM: {self.nome.upper()}")
        print("=-"*40 + "=")
        print(f"Raça: {self.raca.nome if self.raca else 'Não definida'} | Classe: {self.classe.nome if self.classe else 'Não definida'} | Nível: {self.nivel}")
        print("=-"*40 + "=" + "\n" + "\n" + "=-"*40 + "=")
        print("Atributos:")
        for attr, data in self.atributos.items():
            mod_str = f"+{data['mod']}" if data['mod'] >= 0 else str(data['mod'])
            print(f"  {attr}: {data['valor']:<2} (Mod: {mod_str})")
        print("=-"*40 + "=" + "\n\n" + "=-"*40 + "=")
        
        print(f"Pontos de Vida (PV): {self.pontos_de_vida}")
        print(f"Base de Ataque (BA): +{self.base_de_ataque}")
        print(f"Jogada de Proteção (JP): {self.jogada_de_protecao}")
        print(f"Movimento: {self.movimento}m | Infravisão: {self.infravisao}")
        print("=-"*40 + "=" + "\n\n" + "=-"*40 + "=")
        
        if self.proficiencias:
            print("Proficiências:")
            for p in self.proficiencias: print(f"- {p}")
            print("=-"*40 + "=" + "\n\n" + "=-"*40 + "=")
        
        if self.habilidades:
            print("Habilidades Especiais:")
            for h in self.habilidades: print(f"- {h}")
            print("=-"*40 + "=" + "\n\n" + "=-"*40 + "=")    
        
        if self.restricoes:
            print("Restrições:")
            for r in self.restricoes: print(f"- {r}")
            print("=-"*40 + "=" + "\n\n" + "=-"*40 + "=")
        
        if self.notas:
            print("Notas:")
            for n in self.notas: print(f"- {n}")
            print("=-"*40 + "=")
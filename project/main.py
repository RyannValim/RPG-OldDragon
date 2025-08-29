from personagem import Personagem
from racas import Humano, Elfo, Anao
from classes import Guerreiro, Clerigo, Mago

def main():
    nome = input("Insira o nome do seu personagem: ").strip()
    
    personagem = Personagem(nome)

# region Definição dos atributos
    print(f"\nOlá {nome}! Escolha o método para gerar os atributos (1, 2 ou 3):")
    print("     " + "1. Estilo Clássico (rola 3d6 em ordem para cada atributo)")
    print("     " + "2. Estilo Aventureiro (rola 3d6 seis vezes e distribui os valores)")
    print("     " + "3. Estilo Heróico (rola 4d6, descarta o menor, e distribui os valores)")
    
    estilo_escolhido = 0
    while estilo_escolhido not in [1, 2, 3]:
        try:
            estilo_escolhido = int(input("Sua escolha: "))
            if estilo_escolhido not in [1, 2, 3]:
                print("Opção inválida! Selecione um número entre '1, 2 ou 3'.")
        except ValueError:
            print("Erro: Você precisa inserir um número!")
    
    personagem.definir_atributos(estilo_escolhido)
# endregion

# region Escolha da raça
    print("\nEscolha a raça do seu personagem (1, 2 ou 3):")
    print("1. Humano")
    print("2. Elfo")
    print("3. Anão")
    
    racas_disponiveis = {1: Humano(), 2: Elfo(), 3: Anao()}
    raca_escolhida = 0
    while raca_escolhida not in racas_disponiveis:
        try:
            raca_escolhida = int(input("Sua escolha: "))
            if raca_escolhida not in racas_disponiveis:
                print("Opção inválida! Selecione um número entre '1, 2 ou 3'.")
        except ValueError:
            print("Erro: Você precisa inserir um número!")
            
    personagem.raca = racas_disponiveis[raca_escolhida]
    personagem.raca.aplicar_habilidades_raciais(personagem)
# endregion

# region Escolha da classe
    print("\nEscolha a classe do seu personagem (1, 2 ou 3):")
    print("1. Guerreiro")
    print("2. Clérigo")
    print("3. Mago")
    
    classes_disponiveis = {1: Guerreiro(), 2: Clerigo(), 3: Mago()}
    classe_escolhida = 0
    while classe_escolhida not in classes_disponiveis:
        try:
            classe_escolhida = int(input("Sua escolha: "))
            if classe_escolhida not in classes_disponiveis:
                print("Opção inválida! Selecione um número entre '1, 2 ou 3'.")
        except ValueError:
            print("Erro: Você precisa inserir um número!")
            
    personagem.classe = classes_disponiveis[classe_escolhida]
    personagem.classe.aplicar_bonus_de_classe(personagem)
# endregion

    personagem.exibir_ficha()

if __name__ == "__main__":
    main()
from Personagem import Personagem

def main():
    #CRIACAO PERSONAGEM
    nome = input("Insira o nome do seu personagem: ").strip()
    mestre = Personagem(nome)
    #FIM

    #MENU
    print(f"\n{nome}, insira qual o tipo de aventura o grupo pretende jogar?")
    print(" 1. Estilo Clássico")
    print(" 2. Estilo Aventureiro")
    print(" 3. Estilo Heróico")

    estilo_escolhido = 0
    while estilo_escolhido not in [1, 2, 3]:
        try:
            estilo_escolhido = int(input("\nSua escolha (1, 2, 3): "))
            if estilo_escolhido not in [1, 2, 3]:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    #FIM

    #CHAMADA DOS METODOS COM BASE NA ESCOLHA
    match estilo_escolhido:
        case 1:
            print(f"\nDistribuindo atributos para o estilo Clássico...")
            mestre.estilo_classico()
        case 2:
            print(f"\nDistribuindo atributos para o estilo Aventureiro...")
            mestre.estilo_aventureiro()
        case 3:
            print(f"\nDistribuindo atributos para o estilo Heróico...")
            mestre.estilo_heroico()
    #FIM

    #EXIBINDO O PERSONAGEM FINAL
    print(mestre)
    #FIM

if __name__ == "__main__":
    main()
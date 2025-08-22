from Personagem import Personagem

def main():
    """
    Função principal para interagir com o usuário e criar o personagem.
    """
    # CRIACAO PERSONAGEM
    nome = input("Insira o nome do seu personagem: ").strip()
    mestre = Personagem(nome)
    # FIM CRIACAO PERSONAGEM

    # MENU
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

    # FIM MENU

    # CHAMADA DOS METODOS COM BASE NA ESCOLHA
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
    
    # Exibir o personagem final
    print("\n" + "#" * 35)
    print(" " * 10 + "FICHA DO PERSONAGEM")
    print("#" * 35)
    print(mestre)
    print("#" * 35)


if __name__ == "__main__":
    main()
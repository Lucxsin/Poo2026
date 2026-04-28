from classes import Jogador, Equipe

lista_jogadores = []
lista_equipes = []

while True:
    print("\n--- MENU CAMPEONATO ---")
    print("1. Cadastrar jogador")
    print("2. Cadastrar equipe")
    print("3. Adicionar jogador a uma equipe")
    print("4. Listar todas as equipes")
    print("5. Listar jogadores de uma equipe")
    print("6. Buscar jogador por nickname")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        nick = input("Nickname: ")
        turma = input("Turma: ")
        novo_j = Jogador(nome, nick, turma)
        lista_jogadores.append(novo_j)
        print("Jogador cadastrado!")

    elif opcao == "2":
        nome_e = input("Nome da equipe: ")
        jogo = input("Jogo: ")
        nova_e = Equipe(nome_e, jogo)
        lista_equipes.append(nova_e)
        print("Equipe cadastrada!")

    elif opcao == "3":
        # Mostra os jogadores
        for i in range(len(lista_jogadores)):
            print(f"{i} - {lista_jogadores[i].nickname}")
        indice_j = int(input("Número do jogador: "))
        
        # Mostra as equipes
        for i in range(len(lista_equipes)):
            print(f"{i} - {lista_equipes[i].nome_Equipe}")
        indice_e = int(input("Número da equipe: "))

        # Pega o jogador e coloca na equipe
        jogador_escolhido = lista_jogadores[indice_j]
        lista_equipes[indice_e].cadastrarJogador(jogador_escolhido)
        print("Jogador adicionado com sucesso!")

    elif opcao == "4":
        for e in lista_equipes:
            print(f"Equipe: {e.nome_Equipe} | Jogo: {e.jogo} | Qtd: {len(e.jogadores)}")

    elif opcao == "5":
        for i in range(len(lista_equipes)):
            print(f"{i} - {lista_equipes[i].nome_Equipe}")
        indice = int(input("Número da equipe: "))
        lista_equipes[indice].exibirEquipe()

    elif opcao == "6":
        busca = input("Nickname para buscar: ")
        for j in lista_jogadores:
            if j.nickname == busca:
                print(f"Encontrado: {j.nome} da turma {j.turma}")

    elif opcao == "0":
        break

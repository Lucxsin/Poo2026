from classes import Jogador, Equipe

lista_jogadores = []
lista_equipes = []

def buscar_jogador_por_nick(nick):
    for j in lista_jogadores:
        if j.nickname.lower() == nick.lower():
            return j
    return None

while True:
    print("\n" + "="*40)
    print("   CAMPEONATO INTERCLASSE DE E-SPORTS")
    print("="*40)
    print("1. Cadastrar jogador")
    print("2. Cadastrar equipe")
    print("3. Adicionar jogador a uma equipe")
    print("4. Listar todas as equipes")
    print("5. Listar jogadores de uma equipe")
    print("6. Buscar jogador por nickname")
    print("0. Sair")
    print("="*40)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Cadastrar Jogador ---")
        nome = input("Nome: ")
        nick = input("Nickname: ")
        
        if buscar_jogador_por_nick(nick):
            print("Erro: Já existe um jogador com este nickname!")
        else:
            turma = input("Turma: ")
            novo_j = Jogador(nome, nick, turma)
            lista_jogadores.append(novo_j)
            print("Jogador cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- Cadastrar Equipe ---")
        nome_e = input("Nome da equipe: ")
        jogo = input("Jogo: ")
        nova_e = Equipe(nome_e, jogo)
        lista_equipes.append(nova_e)
        print("Equipe cadastrada com sucesso!")

    elif opcao == "3":
        print("\n--- Adicionar Jogador a uma Equipe ---")
        if len(lista_jogadores) == 0 or len(lista_equipes) == 0:
            print("Erro: Cadastre pelo menos um jogador e uma equipe primeiro.")
        else:
            # Listar Jogadores
            print("\nJogadores cadastrados:")
            for i in range(len(lista_jogadores)):
                print(f"{i+1}. {lista_jogadores[i]}")
            
            resp_j = input("Escolha o número do jogador: ")
            
            # Validação manual do índice do jogador
            if resp_j.isdigit():
                idx_j = int(resp_j) - 1
                if 0 <= idx_j < len(lista_jogadores):
                    
                    # Listar Equipes
                    print("\nEquipes cadastradas:")
                    for i in range(len(lista_equipes)):
                        print(f"{i+1}. {lista_equipes[i].nome_equipe}")
                    
                    resp_e = input("Escolha o número da equipe: ")
                    
                    # Validação manual do índice da equipe
                    if resp_e.isdigit():
                        idx_e = int(resp_e) - 1
                        if 0 <= idx_e < len(lista_equipes):
                            
                            jogador_sel = lista_jogadores[idx_j]
                            equipe_sel = lista_equipes[idx_e]

                            # Verificar se já está em alguma equipe
                            ja_tem_equipe = False
                            for e in lista_equipes:
                                if jogador_sel in e.jogadores:
                                    ja_tem_equipe = True
                            
                            if ja_tem_equipe:
                                print(f"Erro: {jogador_sel.nickname} já está em uma equipe!")
                            else:
                                if equipe_sel.cadastrar_jogador(jogador_sel):
                                    print("Sucesso: Jogador adicionado!")
                        else:
                            print("Erro: Número de equipe inválido!")
                    else:
                        print("Erro: Digite apenas números!")
                else:
                    print("Erro: Número de jogador inválido!")
            else:
                print("Erro: Digite apenas números!")

    elif opcao == "4":
        print("\n--- Listagem de Equipes ---")
        if not lista_equipes:
            print("Nenhuma equipe cadastrada.")
        else:
            for e in lista_equipes:
                print(f"Equipe: {e.nome_equipe} | Jogo: {e.jogo} | Jogadores: {len(e.jogadores)}/5")

    elif opcao == "5":
        print("\n--- Jogadores da Equipe ---")
        if not lista_equipes:
            print("Nenhuma equipe cadastrada.")
        else:
            for i in range(len(lista_equipes)):
                print(f"{i+1}. {lista_equipes[i].nome_equipe}")
            
            resp = input("Escolha o número da equipe: ")
            if resp.isdigit():
                idx = int(resp) - 1
                if 0 <= idx < len(lista_equipes):
                    lista_equipes[idx].exibir_equipe()
                else:
                    print("Equipe não encontrada!")
            else:
                print("Erro: Digite um número!")

    elif opcao == "6":
        nick_busca = input("Digite o nickname: ")
        j = buscar_jogador_por_nick(nick_busca)
        if j:
            print(f"Jogador: {j}")
        else:
            print("Jogador não encontrado.")

    elif opcao == "0":
        print("Saindo... Boa sorte no campeonato!")
        break
    else:
        print("Opção inválida!")

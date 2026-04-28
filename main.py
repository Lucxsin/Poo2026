class Jogador:
    def __init__(self, nome, nickname, turma):
        self.nome = nome
        self.nickname = nickname
        self.turma = turma

    def __str__(self):
        return f"{self.nome} ({self.nickname}) - {self.turma}"


class Equipe:
    def __init__(self, nome_equipe, jogo):
        self.nome_equipe = nome_equipe
        self.jogo = jogo
        self.jogadores = [] 

    def cadastrar_jogador(self, jogador):
        
        if len(self.jogadores) < 5:
            self.jogadores.append(jogador)
            return True
        else:
            print(f"Erro: A equipe {self.nome_equipe} já está cheia (limite 5)!")
            return False

    def exibir_equipe(self):
        print(f"\nEquipe: {self.nome_equipe} | Jogo: {self.jogo}")
        print(f"Total de jogadores: {len(self.jogadores)}")
        if self.jogadores:
            print("Jogadores:")
            for j in self.jogadores:
                print(f"  - {j}")
        else:
            print("  (Nenhum jogador cadastrado nesta equipe)")

class Jogador:
    def __init__(self, nome, nickname, turma):
        self.nome = nome
        self.nickname = nickname
        self.turma = turma

class Equipe:
    def __init__(self, nome_Equipe, jogo):
        self.nome_Equipe = nome_Equipe
        self.jogo = jogo
        self.jogadores = [] # Lista que vai guardar os objetos Jogador


    def cadastrarJogador(self, um_jogador):
        if len(self.jogadores) < 5:
            self.jogadores.append(um_jogador)
            return True
        else:
            print("Equipe lotada")
            return False

    def exibirEquipe(self):
        print(f"\nEquipe: {self.nome_Equipe} | Jogo: {self.jogo}")
        print("Integrantes:")
        for j in self.jogadores:
            print(f"- {j.nome} ({j.nickname}) da turma {j.turma}")

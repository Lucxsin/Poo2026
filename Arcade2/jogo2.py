import arcade
import random

# -----------------------------
# CONFIGURAÇÕES
# -----------------------------
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO = "Coletor de Tesouros"

VELOCIDADE_PLAYER = 5
QUANTIDADE_MOEDAS = 25

# CAMINHOS DAS IMAGENS
CAMINHO_PLAYER_DIREITA = "jogadora_right.png"
CAMINHO_PLAYER_ESQUERDA = "jogadora_left.png"

CAMINHO_MOEDA = "strawberry.png"
CAMINHO_MOEDA_ESPECIAL = "diamante.png"

CAMINHO_INIMIGO = "azul.png"
CAMINHO_INIMIGO_ESPECIAL = "amarelo.png"


# -----------------------------
# PLAYER
# -----------------------------
class Player(arcade.Sprite):

    def __init__(self) -> None:

        super().__init__(CAMINHO_PLAYER_DIREITA, scale=0.15)

        self.textura_direita = arcade.load_texture(
            CAMINHO_PLAYER_DIREITA
        )

        self.textura_esquerda = arcade.load_texture(
            CAMINHO_PLAYER_ESQUERDA
        )

    def update(
        self,
        delta_time: float = 1/60
    ) -> None:

        self.center_x += self.change_x
        self.center_y += self.change_y

        # limites da tela
        if self.left < 0:
            self.left = 0

        if self.right > LARGURA_TELA:
            self.right = LARGURA_TELA

        if self.bottom < 0:
            self.bottom = 0

        if self.top > ALTURA_TELA:
            self.top = ALTURA_TELA

        # trocar textura
        if self.change_x < 0:
            self.texture = self.textura_esquerda

        elif self.change_x > 0:
            self.texture = self.textura_direita


# -----------------------------
# MOEDA NORMAL
# -----------------------------
class Moeda(arcade.Sprite):

    def __init__(self) -> None:

        super().__init__(CAMINHO_MOEDA, scale=0.08)


# -----------------------------
# MOEDA ESPECIAL
# -----------------------------
class MoedaEspecial(arcade.Sprite):

    def __init__(self) -> None:

        super().__init__(CAMINHO_MOEDA_ESPECIAL, scale=0.10)

        self.change_x = random.choice([-4, 4])
        self.change_y = random.choice([-4, 4])

    def update(
        self,
        delta_time: float = 1/60
    ) -> None:

        self.center_x += self.change_x
        self.center_y += self.change_y

        # rebote
        if self.left <= 0 or self.right >= LARGURA_TELA:
            self.change_x *= -1

        if self.bottom <= 0 or self.top >= ALTURA_TELA:
            self.change_y *= -1


# -----------------------------
# INIMIGO NORMAL
# -----------------------------
class Inimigo(arcade.Sprite):

    def __init__(self) -> None:

        super().__init__(CAMINHO_INIMIGO, scale=0.12)

        self.change_x = random.choice([-3, 3])
        self.change_y = random.choice([-3, 3])

    def update(
        self,
        delta_time: float = 1/60
    ) -> None:

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left <= 0 or self.right >= LARGURA_TELA:
            self.change_x *= -1

        if self.bottom <= 0 or self.top >= ALTURA_TELA:
            self.change_y *= -1


# -----------------------------
# INIMIGO ESPECIAL
# -----------------------------
class InimigoEspecial(arcade.Sprite):

    def __init__(self) -> None:

        super().__init__(CAMINHO_INIMIGO_ESPECIAL, scale=0.12)

        self.change_x = random.choice([-5, 5])
        self.change_y = random.choice([-5, 5])

    def update(
        self,
        delta_time: float = 1/60
    ) -> None:

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left <= 0 or self.right >= LARGURA_TELA:
            self.change_x *= -1

        if self.bottom <= 0 or self.top >= ALTURA_TELA:
            self.change_y *= -1


# -----------------------------
# JANELA DO JOGO
# -----------------------------
class JanelaJogo(arcade.Window):

    def __init__(self) -> None:

        super().__init__(
            LARGURA_TELA,
            ALTURA_TELA,
            TITULO
        )

        arcade.set_background_color(
            arcade.color.AMAZON
        )

        self.player_lista = arcade.SpriteList()
        self.moedas_lista = arcade.SpriteList()
        self.moeda_especial_lista = arcade.SpriteList()
        self.inimigo_lista = arcade.SpriteList()
        self.inimigo_especial_lista = arcade.SpriteList()

        self.player = None

        self.pontos = 0

        self.mensagem = ""
        self.tempo_mensagem = 0

        self.fim_jogo = False

    def setup(self) -> None:

        # PLAYER
        self.player = Player()

        self.player.center_x = 400
        self.player.center_y = 300

        self.player_lista.append(self.player)

        # MOEDAS
        for i in range(QUANTIDADE_MOEDAS):

            moeda = Moeda()

            moeda.center_x = random.randint(50, 750)
            moeda.center_y = random.randint(50, 550)

            self.moedas_lista.append(moeda)

        # MOEDA ESPECIAL
        moeda_especial = MoedaEspecial()

        moeda_especial.center_x = 200
        moeda_especial.center_y = 200

        self.moeda_especial_lista.append(
            moeda_especial
        )

        # INIMIGO NORMAL
        inimigo = Inimigo()

        inimigo.center_x = 600
        inimigo.center_y = 400

        self.inimigo_lista.append(inimigo)

        # INIMIGO ESPECIAL
        inimigo_especial = InimigoEspecial()

        inimigo_especial.center_x = 150
        inimigo_especial.center_y = 450

        self.inimigo_especial_lista.append(
            inimigo_especial
        )

    def on_draw(self) -> None:

        self.clear()

        # desenhar sprites
        self.player_lista.draw()
        self.moedas_lista.draw()
        self.moeda_especial_lista.draw()
        self.inimigo_lista.draw()
        self.inimigo_especial_lista.draw()

        # HUD
        arcade.draw_text(
            f"Pontos: {self.pontos}",
            10,
            560,
            arcade.color.WHITE,
            22
        )

        # mensagem dano
        if self.tempo_mensagem > 0:

            arcade.draw_text(
                self.mensagem,
                180,
                520,
                arcade.color.RED,
                24
            )

        # tela final
        if self.fim_jogo:

            arcade.draw_text(
                "FIM DE JOGO",
                250,
                320,
                arcade.color.WHITE,
                40
            )

            arcade.draw_text(
                f"Pontuação Final: {self.pontos}",
                220,
                250,
                arcade.color.YELLOW,
                30
            )

    def on_update(
        self,
        delta_time: float
    ) -> None:

        if self.fim_jogo:
            return

        # updates
        self.player_lista.update()
        self.moeda_especial_lista.update()
        self.inimigo_lista.update()
        self.inimigo_especial_lista.update()

        # colisão moedas normais
        moedas_colididas = arcade.check_for_collision_with_list(
            self.player,
            self.moedas_lista
        )

        for moeda in moedas_colididas:

            moeda.remove_from_sprite_lists()

            self.pontos += 1

        # colisão moeda especial
        especiais = arcade.check_for_collision_with_list(
            self.player,
            self.moeda_especial_lista
        )

        for moeda in especiais:

            moeda.remove_from_sprite_lists()

            self.pontos += 5

        # colisão inimigo normal
        inimigos = arcade.check_for_collision_with_list(
            self.player,
            self.inimigo_lista
        )

        if len(inimigos) > 0:

            self.pontos -= 1

            self.mensagem = (
                "Cuidado! Você foi atingido!"
            )

            self.tempo_mensagem = 60

        # colisão inimigo especial
        inimigos_especiais = arcade.check_for_collision_with_list(
            self.player,
            self.inimigo_especial_lista
        )

        for inimigo in inimigos_especiais:

            self.pontos -= 1

            inimigo.remove_from_sprite_lists()

            novo = InimigoEspecial()

            novo.center_x = random.randint(50, 750)
            novo.center_y = random.randint(50, 550)

            self.inimigo_especial_lista.append(
                novo
            )

        # diminuir tempo mensagem
        if self.tempo_mensagem > 0:
            self.tempo_mensagem -= 1

        # fim do jogo
        if (
            len(self.moedas_lista) == 0
            and
            len(self.moeda_especial_lista) == 0
        ):
            self.fim_jogo = True

    def on_key_press(
        self,
        key: int,
        modifiers: int
    ) -> None:

        # WASD
        if key == arcade.key.W:
            self.player.change_y = VELOCIDADE_PLAYER

        if key == arcade.key.S:
            self.player.change_y = -VELOCIDADE_PLAYER

        if key == arcade.key.A:
            self.player.change_x = -VELOCIDADE_PLAYER

        if key == arcade.key.D:
            self.player.change_x = VELOCIDADE_PLAYER

        # SETAS
        if key == arcade.key.UP:
            self.player.change_y = VELOCIDADE_PLAYER

        if key == arcade.key.DOWN:
            self.player.change_y = -VELOCIDADE_PLAYER

        if key == arcade.key.LEFT:
            self.player.change_x = -VELOCIDADE_PLAYER

        if key == arcade.key.RIGHT:
            self.player.change_x = VELOCIDADE_PLAYER

        # ESC
        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(
        self,
        key: int,
        modifiers: int
    ) -> None:

        if key in (
            arcade.key.W,
            arcade.key.S,
            arcade.key.UP,
            arcade.key.DOWN
        ):

            self.player.change_y = 0

        if key in (
            arcade.key.A,
            arcade.key.D,
            arcade.key.LEFT,
            arcade.key.RIGHT
        ):

            self.player.change_x = 0


# -----------------------------
# MAIN
# -----------------------------
def main() -> None:

    jogo = JanelaJogo()

    jogo.setup()

    arcade.run()


if __name__ == "__main__":
    main()
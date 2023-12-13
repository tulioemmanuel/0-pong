import pygame
import logging
from base.system import System
from base.configuration import Configuration


class Renderer(System):
    def __init__(self, game):
        self.game = game
        self.setup()

    def setup(self):
        super().setup()
        self.settings = Configuration().settings
        pygame.display.set_caption(self.settings["title"])
        self.screen = pygame.display.set_mode(
            (self.settings["screen_width"], self.settings["screen_height"])
        )

        if not pygame.font.get_init():
            pygame.font.init()

        self.font = pygame.font.SysFont("Comic Sans MS", 24)

        logging.info("Renderer initialized")

    def _clear(self):
        screen = self.screen
        screen.fill(
            (self.settings["bg_r"], self.settings["bg_g"], self.settings["bg_b"])
        )
        stripe_w = int(self.settings["stripes_w"])
        stripe_h = int(self.settings["stripes_h"])
        x = screen.get_width() / 2 - int(stripe_w) / 2
        y = 0
        while y <= screen.get_height():
            screen.fill((255, 255, 255), pygame.Rect(x, y, stripe_w, stripe_h))
            y += int(self.settings["stripes_offset"])

    def update_points(self):
        self._draw_points()

    def _draw_points(self):
        player_points_txt = self.font.render(
            str(self.game.player_points),
            False,
            (
                self.settings["points_color_r"],
                self.settings["points_color_g"],
                self.settings["points_color_b"],
            ),
        )
        enemy_points_txt = self.font.render(
            str(self.game.enemy_points),
            False,
            (
                self.settings["points_color_r"],
                self.settings["points_color_g"],
                self.settings["points_color_b"],
            ),
        )

        self.screen.blit(
            player_points_txt,
            (self.screen.get_width() / 4 - player_points_txt.get_width() / 2, 10),
        )
        self.screen.blit(
            enemy_points_txt,
            (
                3 * self.screen.get_width() / 4 - 3 * enemy_points_txt.get_width() / 2,
                10,
            ),
        )

    def draw(self):
        self._clear()
        self.screen.blit(
            self.game.player.image, (self.game.player.rect.x, self.game.player.rect.y)
        )
        self.screen.blit(
            self.game.enemy.image, (self.game.enemy.rect.x, self.game.enemy.rect.y)
        )
        self.screen.blit(
            self.game.ball.image, (self.game.ball.rect.x, self.game.ball.rect.y)
        )

        self._draw_points()

        pygame.display.flip()
        pygame.display.update()

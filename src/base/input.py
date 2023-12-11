import pygame
import logging
from base.system import System


class Input(System):
    def __init__(self, game):
        self.game = game
        self.setup()

    def setup(self):
        super().setup()
        logging.info("Input initialized")

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.quit()
                elif event.key == pygame.K_w:
                    self.game.player.move_up()
                elif event.key == pygame.K_s:
                    self.game.player.move_down()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.game.player.stop()

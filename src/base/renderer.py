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
        logging.info("Renderer initialized")

    def _clear(self):
        self.screen.fill((self.settings['bg_r'], self.settings['bg_g'], self.settings['bg_b']))

    def draw(self):
        self._clear()
        self.screen.blit(self.game.player.image,(self.game.player.x,self.game.player.y))
        self.screen.blit(self.game.player.image,(self.screen.get_width() - 20 ,self.game.player.y))
        self.screen.blit(pygame.Surface((10,10)),(self.screen.get_width() / 2 - 5,self.screen.get_height() / 2 - 5))
        
        pygame.display.flip()
        pygame.display.update()

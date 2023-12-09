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
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                self.game.running = False

import pygame
from pygame.sprite import Sprite
from base.configuration import Configuration

class Paddle(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        settings = Configuration().settings
        surface = pygame.Surface((settings['paddle_width'],settings['paddle_height']))
        surface.fill((255,255,255))
        self.image = surface
        self.x = 10
        self.y = 100
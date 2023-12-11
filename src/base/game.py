import pygame
from base.renderer import Renderer
from base.input import Input
from base.configuration import Configuration


class Game(object):
    def __init__(self):
        self.renderer = Renderer(self)
        self.input = Input(self)
        self.configuration = Configuration()
        self.clock = pygame.time.Clock()
        self.setup()

    def setup(self):
        pygame.init()
        pygame.font.init()
        self.running = True

    def update(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    async def mainloop(self):
        raise NotImplementedError

    def quit(self):
        self.running = False

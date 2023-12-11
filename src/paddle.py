from typing import Any
import pygame
from base.entity import Entity


class Paddle(Entity):
    def __init__(self, name="paddle", x=0, y=0):
        Entity.__init__(self)
        self.name = name
        surface = pygame.Surface(
            (self.settings["paddle_width"], self.settings["paddle_height"])
        )
        surface.fill(
            (
                self.settings["paddle_color_r"],
                self.settings["paddle_color_g"],
                self.settings["paddle_color_b"],
            )
        )
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vy = 0

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.rect.y += self.vy

    def move_up(self):
        self.vy -= self.settings["paddle_vy"]

    def move_down(self):
        self.vy += self.settings["paddle_vy"]

    def stop(self):
        self.vy = 0

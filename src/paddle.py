import logging
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
        self.init_x = x
        self.init_y = y
        self.rect.x = x
        self.rect.y = y
        self.vy = 0
        self.ai_should_react = False
        self.screen = pygame.display.get_surface()

    def ai_update(self, delta, ball):
        speed = self.settings["paddle_vy"]
        if self.ai_should_react:
            if ball.rect.y >= self.rect.y + self.rect.height / 2:
                if (
                    self.rect.y + self.rect.height
                    <= pygame.display.get_surface().get_height()
                ):
                    self.vy = speed
            else:
                if self.rect.y >= 0:
                    self.vy = -speed
            self.update()

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self.rect.y += self.vy

    def move_up(self):
        self.vy -= self.settings["paddle_vy"]

    def move_down(self):
        self.vy += self.settings["paddle_vy"]

    def move_touch(self, pos):
        if pos[1] >= self.screen.get_height()/2:
            self.move_down()
        else:
            self.move_up()            

    def stop(self):
        self.vy = 0

    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y

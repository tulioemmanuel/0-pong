import pygame
from pygame.sprite import Group
from base.entity import Entity


class Ball(Entity):
    def __init__(self, game):
        Entity.__init__(self)
        surface = pygame.Surface(
            (self.settings["ball_size"], self.settings["ball_size"])
        )
        surface.fill(
            (
                self.settings["ball_color_r"],
                self.settings["ball_color_g"],
                self.settings["ball_color_b"],
            )
        )
        self.paddles = Group(game.player, game.enemy)
        self.game = game
        self.image = surface
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = (
            pygame.display.get_surface().get_width() / 2 - self.image.get_width() / 2
        )
        self.rect.y = (
            pygame.display.get_surface().get_height() / 2 - self.image.get_height() / 2
        )
        self.vx = -5
        self.vy = 0

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.check_collision()

    def check_collision(self):
        paddle = pygame.sprite.spritecollide(self, self.paddles, False)
        if paddle:
            if paddle[0].name == "player":
                self.rect.x = paddle[0].rect.x + self.rect.w
                self.vx = 5
            else:
                self.vx = -5
                self.rect.x = paddle[0].rect.x - self.rect.w

        if self.rect.x == -self.rect.w:
            self.game.add_point("enemy")
            self.reset()
        elif self.rect.x == self.game.renderer.screen.get_width() + self.rect.w:
            self.game.add_point("player")
            self.reset()

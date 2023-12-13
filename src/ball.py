import pygame
import math
import random
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
        self.ball_speed = int(self.settings["ball_speed"])
        self.reset()

    def reset(self):
        self.rect.x = (
            pygame.display.get_surface().get_width() / 2 - self.image.get_width() / 2
        )
        self.rect.y = (
            pygame.display.get_surface().get_height() / 2 - self.image.get_height() / 2
        )
        self.vx = (1 if random.random() >= 0.5 else -1) * self.ball_speed
        self.vy = 0

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.check_collision()

    def check_collision(self):
        paddle = pygame.sprite.spritecollide(self, self.paddles, False)
        if paddle:
            self.change_direction(paddle[0])
            return

        if self.rect.x <= -self.rect.w:
            self.game.add_point("enemy")
        elif self.rect.x >= self.game.renderer.screen.get_width():
            self.game.add_point("player")
        elif self.rect.y <= 0 or self.rect.y + self.rect.h > pygame.display.get_surface().get_height():
            self.vy *= -1
        

    def change_direction(self, paddle):
        paddle_hit_y = paddle.rect.y
        ball_hit_y = self.rect.y
        percentage = (paddle.rect.h + paddle_hit_y - ball_hit_y) / (paddle.rect.h)
        
        if paddle.name == "player":
            self.rect.x = paddle.rect.x + self.rect.w
            self.vx = self.ball_speed * math.cos(percentage)
            self.game.enemy.ai_should_react = True
        else:
            self.vx = -self.ball_speed * math.cos(percentage)
            self.rect.x = paddle.rect.x - self.rect.w
            self.game.enemy.ai_should_react = False
        self.vy = (-1 if percentage >= .5 else 1) * self.ball_speed * math.sin(percentage)

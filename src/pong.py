import pygame
from base.game import Game
from base.configuration import Configuration
from paddle import Paddle
from ball import Ball


class Pong(Game):
    def __init__(self):
        super().__init__()
        self.setup()
        self.mainloop()

    def setup(self):
        super().setup()
        self.settings = Configuration().settings
        self.frame_delta = 0
        self.player = Paddle(
            "player",
            10,
            self.settings["screen_height"] / 2 - self.settings["paddle_height"] / 2,
        )
        self.enemy = Paddle(
            "enemy",
            self.renderer.screen.get_width() - 20,
            self.settings["screen_height"] / 2 - self.settings["paddle_height"] / 2,
        )
        self.ball = Ball(self)
        self.player_points = 0
        self.enemy_points = 0
        self.renderer.update_points()

    def add_point(self, who):
        if who == "player":
            self.player_points += 1
        else:
            self.enemy_points += 1
        self.reset_game()            
    
    def reset_game(self):
        self.player.reset()
        self.enemy.reset()
        self.ball.reset()

    def update(self):
        self.player.update()
        self.enemy.ai_update(self.frame_delta,self.ball)
        self.ball.update()

    def render(self):
        self.renderer.draw()

    def mainloop(self):
        self.input.get_input()
        self.update()
        self.render()
        self.frame_delta = self.clock.tick(self.settings["FPS"])

    def cleanup(self):
        pygame.font.init()
        pygame.quit()

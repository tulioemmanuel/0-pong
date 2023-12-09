from base.game import Game
from base.configuration import Configuration
from paddle import Paddle


class Pong(Game):
    def __init__(self):
        super().__init__()
        self.setup()
        self.mainloop()

    def setup(self):
        super().setup()
        self.settings = Configuration().settings
        self.frame_delta = 0
        self.player = Paddle()

    def update(self):
        pass

    def render(self):
        self.renderer.draw()

    def mainloop(self):
        self.input.get_input()
        self.update()
        self.render()
        self.frame_delta = self.clock.tick(self.settings["FPS"])

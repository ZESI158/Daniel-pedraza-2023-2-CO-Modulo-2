import random

from dino_runner.components.obstacles.obstacule import Obstacule


class Cactus(Obstacule):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__( image, self.type)
        self.rect.y = 315
        self.rect.x = random.choice(range(2000,4000))


class Bird(Obstacule):
    def __init__(self, image):
            self.type = random.randint(0,1)
            super().__init__(image, self.type)
            self.rect.y = random.choice(range(200, 350, 250))
            self.rect.x = 1100 
import random

from dino_runner.components.obstacles.obstacule import Obstacule

class Cactus(Obstacule):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325
        

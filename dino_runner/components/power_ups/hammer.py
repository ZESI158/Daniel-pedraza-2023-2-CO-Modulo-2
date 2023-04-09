import random
import pygame

from dino_runner.components.power_ups.power_up  import PowerUP
from dino_runner.utils.constants import  HAMMER_TYPE, HAMMER


class Hammer(PowerUP):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
        self.rect.y = random.randint(200,300)
        print("power")
    





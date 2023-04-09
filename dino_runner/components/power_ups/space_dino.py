import random
import pygame
import math

from dino_runner.components.power_ups.power_up  import PowerUP
from dino_runner.utils.constants import  SPACE_TYPE,  SPACE, SCREEN_HEIGHT, SCREEN_WIDTH


class Space(PowerUP):
    def __init__(self):
        super().__init__(SPACE, SPACE_TYPE)
        print("nave")


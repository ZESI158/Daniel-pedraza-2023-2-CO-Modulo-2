import pygame
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.space_dino import Space 
from dino_runner.utils.constants import SPACE_TYPE, HAMMER_TYPE, HAMMER



class PowerUpManager:
    def __init__(self) -> None:
        self.power_ups = []
        self.when_appears = random.randint(150,250)
        self.image = HAMMER
        self.duration = random.randint(3,5)
    def generate_power_ups(self, power_type):
        self.when_appears += random.randint(150,250)
        if power_type == 0:
            power = Shield()
            return power
        elif power_type == 1:
            power = Space()
            return power
        else:
            power = Hammer()
            return power

        

# obstacle = self.generate_obstacle(obstacle_type)
    #   self.obstacles.append(obstacle)
    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            power_generer = random.randint(0, 4)
            powers = self.generate_power_ups(power_generer)
            self.power_ups.append(powers)

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration *1000)
                self.power_ups.remove(power_up)

    def hammer(self,game):
        if game.player.type == HAMMER_TYPE:
                print("shot")
    def space(self, game):
        if game.player.type == SPACE_TYPE:
            print("nave")
            game.player.rect = self.image.get_rect()
            game.player.dino_rect.y = 20
            game.player.dino_rect.x = 0

    def active_power(self):
        acciones = {
        "HAMMER_TYPE": self.hammer,
        "SHIELD_TYPE": self.space,
    }        
    



    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

        

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(150,250)
        self.duration = random.randint(3,5)

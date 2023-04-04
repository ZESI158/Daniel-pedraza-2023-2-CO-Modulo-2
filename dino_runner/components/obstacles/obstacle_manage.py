import pygame
from dino_runner.components.obstacles.captus import Cactus,  Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def generate_obstacle(self):
        obstacle = Cactus(SMALL_CACTUS)
        return obstacle
    def generate_obstacle1(self):
        obstacle1 = Cactus(LARGE_CACTUS)
        return obstacle1
    def generate_obstacle2(self):
        obstacle1 = Bird(BIRD)
        return obstacle1

    
    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            obstacle1 = self.generate_obstacle1()
            obstacle2 = self.generate_obstacle2()
            self.obstacles.append(obstacle)
            self.obstacles.append(obstacle1)
            self.obstacles.append(obstacle2)
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("collision")
                pygame.time.delay(1000)
                game.playing = False
        
#implementar catus  grandes y aves altura 
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)




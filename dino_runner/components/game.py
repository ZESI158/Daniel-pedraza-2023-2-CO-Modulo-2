import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, CLOUD, GAME_OVER, RESET
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.menu import Menu


class Game:
    Game_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.Game_SPEED
        self.y_pos_cl = 100
        self.x_pos_cl = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('press key start game', self.screen)
        self.player = Dinosaur()
        self.death_count = 0
        self.score = 0
        self.last_score = []
        self.highest_score = 0


    def execute(self):

        self.runnig = True
        while self.runnig:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.game_speed = self.game_speed
        self.player.reset_dinosaur()
        self.reset_speed()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.cloud()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    def cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cl, self.y_pos_cl))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cl, self.y_pos_cl))
        if self.x_pos_cl <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cl, self.y_pos_cl))
            self.x_pos_cl = 1100
        self.x_pos_cl -= self.game_speed

        
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)
        self.highest_score = self.score
        self.last_score.append(self.highest_score)
        scores_max = max(self.last_score)
        if self.death_count  == 0:
            self.menu.draw(self.screen)
        else:
            
            self.menu.update_message(f'Press any Key to restart')
            self.menu.draw(self.screen)

            self.menu.death(f"Total Deaths: {self.death_count}")
            self.menu.draw(self.screen)

            self.menu.max(f"Highest Score: {scores_max}")
            self.menu.draw(self.screen)

            self.menu.scoreboard(f"Your Score: {self.score}")
            self.menu.draw(self.screen)
            self.screen.blit(GAME_OVER,(half_screen_width-180, half_screen_height -200))
            self.screen.blit(BG,(half_screen_width -530, half_screen_height -90 ))
            self.screen.blit(RESET,(half_screen_width -50, half_screen_height -50))

        self.screen.blit(ICON, (half_screen_width -50, half_screen_height -150 ))
        self.menu.update(self)


    def update_score(self):
        self.score +=1

        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score:{self.score}', True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def reset_speed(self):
        self.game_speed = 20
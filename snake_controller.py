import pygame
from sys import exit
from snake_model import *
from snake_view import *

TICK_RATE = 15

pygame.init()
pygame.display.set_caption("Snake")


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.gameWorld = World()
        self.UI = UI(self.gameWorld)
        self.isRun = False

    def game_loop(self):
        while True:
            self.handle_player_input()
            self.UI.draw_hud()

            if self.isRun:
                self.gameWorld.step()

                if self.gameWorld.isCollide:
                    self.isRun = False
                else:
                    self.UI.draw_blocks()

            else:
                self.UI.draw_instructions()

            pygame.display.update()
            self.clock.tick(TICK_RATE)

    def handle_player_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.gameWorld.__init__()
                    self.isRun = True

                elif event.key == pygame.K_UP:
                    self.gameWorld.snake.change_direction(0)
                elif event.key == pygame.K_DOWN:
                    self.gameWorld.snake.change_direction(1)
                elif event.key == pygame.K_LEFT:
                    self.gameWorld.snake.change_direction(2)
                elif event.key == pygame.K_RIGHT:
                    self.gameWorld.snake.change_direction(3)

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

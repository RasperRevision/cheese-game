import pygame
from tiles import Tileset, Tilemap

class Game:
    WIDTH = 1280
    HEIGHT = 720
    SIZE = WIDTH, HEIGHT

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        pygame.display.set_caption("Cheese Game")
        self.clock=pygame.time.Clock()
        
    
    def run(self):
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            key = pygame.key.get_pressed()
            if key[pygame.K_q]:
                self.screen.fill("black")
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


game = Game()

tileset = Tileset("/assets/tileset/")
tilemap = Tilemap(tileset, (8, 8), tileset.rect)

game.run()

import pygame

from logger import log


class Game:
    
    zoom = 1
    WIDTH = 480/zoom
    HEIGHT = 360/zoom
    
    SIZE = WIDTH, HEIGHT

    def __init__(self):
        pygame.init()
        log('Pygame initialised')

        #pygame_border.display.set_caption("Cheese Game")
        self.screen = pygame.display.set_mode(Game.SIZE, 
                                              pygame.SCALED | pygame.FULLSCREEN)
        log('Display initialised')
        self.clock=pygame.time.Clock()


    def getScreen(self):
        return self.screen
    
    def run(self):

        from character import Player
        from tiles import Tilemap, Tileset

        log('Successfully imported classes')
        
        tileset = Tileset("assets/tileset/outside.png")
        tilemap = Tilemap(tileset, 
                          game.getScreen(), 
                          [Game.WIDTH, 
                          Game.HEIGHT])

        log('Tilemap initialised')
        
        player = Player('assets/sprites/player/', 
                        self.screen, 
                        Game.WIDTH, 
                        Game.HEIGHT, 
                        tilemap)

        log('Character controller initialised')
        
        self.running = True
        log('Game running')
        
        while self.running:
            tozoom=False
            Game.WIDTH = 480/Game.zoom
            Game.HEIGHT = 360/Game.zoom
            Game.SIZE = Game.WIDTH,Game.HEIGHT
            if Game.zoom>0.10000000001:
                tozoom=True
          
            self.screen=pygame.transform.scale(self.screen,game.SIZE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_EQUALS]:
                if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
                    Game.zoom += 0.1
                else:
                    Game.zoom = 1
                pygame.display.set_mode(Game.SIZE, pygame.SCALED | pygame.FULLSCREEN)
            if key[pygame.K_MINUS] and tozoom:
                Game.zoom = Game.zoom - 0.1
                print(Game.zoom)
                pygame.display.set_mode(Game.SIZE, pygame.SCALED | pygame.FULLSCREEN)
                
            if key[pygame.K_w]:
                player.move('n')
            if key[pygame.K_s]:
                player.move('s')
            if key[pygame.K_d]:
                player.move('e')
            if key[pygame.K_a]:
                player.move('w')
        
            if key[pygame.K_ESCAPE]:
                self.running=False
            
            
            pygame.display.flip()
            
            self.clock.tick(60)
        pygame.quit()


game = Game()
game.run()

import csv

from numpy import array
from pygame import Rect, Surface, image


class Tileset:
    def __init__(self, file):
        self.file = file
        
        self.image = image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        
        self.load()
    
    def load(self):
        w, h = self.rect.size
        dx = dy = 16
        
        for x in range(0, w//dx):
            for y in range(0, h//dy):
                tile = Surface((dx, dy))
                tile.blit(self.image, (0, 0), area=Rect((x*dx, y*dy), (dx, dy)))
                self.tiles.append(tile)


class Tilemap:
    def __init__(self, tileset, screen, screenSize):
        self.tileset = tileset
        self.screen = screen
        self.screenWidth, self.screenHeight = screenSize

        self.map, self.size = self.get_map('assets/tilemap/map.csv')
        self.rect = tileset.rect
        
        self.positionOffset = [self.screenWidth // 2 - self.size[0] * 8 + 8,
                               self.screenHeight // 2 - self.size[1] * 8 + 8]
        self.position = [self.positionOffset[0], self.positionOffset[1]]


        self.render()


    def render(self):
        self.screen.fill('black')
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                tile = self.tileset.tiles[self.map[i, j]]
                
                self.screen.blit(tile, (j*16+self.position[0], 
                                        i*16+self.position[1]))

    def get_map(self, map):
        with open(map, 'r') as file:
            rows = list(csv.reader(file))
            new_rows = []
            for row in rows:
                new_row = []
                for num in row:
                    new_row.append(int(num))
                new_rows.append(new_row)
                
        a = array(new_rows)
        return (a, a.shape)
            

    def adjustPosition(self, playerPos):
        x, y = playerPos
        self.position = [self.positionOffset[0] - x + self.screenWidth // 2, 
                         self.positionOffset[1] - y + self.screenHeight // 2]
        self.render()
        

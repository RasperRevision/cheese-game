from math import sqrt

import pygame

from camera import Camera
from logger import log


class Player:
  
  SPEED = 1.0
  
  def __init__(self, sprite_path, screen, s_width, s_height, tilemap):
    self.sprite_path_front = sprite_path + 'front-default.png'
    self.sprite_path_back = sprite_path + 'back-default.png'
    self.sprite_path_left = sprite_path + 'left-default.png'
    self.sprite_path_right = sprite_path + 'right-default.png'
    
    self.front_sprite = pygame.image.load(self.sprite_path_front)
    self.back_sprite = pygame.image.load(self.sprite_path_back)
    self.left_sprite = pygame.image.load(self.sprite_path_left)
    self.right_sprite = pygame.image.load(self.sprite_path_right)
    
    self.screen = screen
    self.position = [s_width // 2, s_height // 2]
    self.sprite = self.front_sprite
    self.screen.blit(self.sprite, self.position)
    
    self.camera = Camera(0, 0)
    log("Camera initialised")
    self.tilemap = tilemap

    

  def move(self, direction):
    match direction:
      case 'n':
        self.position[1] -= Player.SPEED
        self.camera.y -= Player.SPEED
        self.sprite = self.back_sprite 
      case 's':
        self.position[1] += Player.SPEED
        self.camera.y += Player.SPEED
        self.sprite = self.front_sprite
      case 'e':
        self.position[0] += Player.SPEED
        self.camera.x += Player.SPEED
        self.sprite = self.right_sprite
      case 'w':
        self.position[0] -= Player.SPEED
        self.camera.x -= Player.SPEED
        self.sprite = self.left_sprite
      case _:
        raise Exception("No third dimension here")
    self.tilemap.adjustPosition(self.position)
    self.screen.blit(self.sprite, (self.position[0] - self.camera.x, 
                                   self.position[1] - self.camera.y))

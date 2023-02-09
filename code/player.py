# player.py
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        ''' Variable Player '''
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y), (TILE_SIZE/2, TILE_SIZE/2))
        self.speed = 300

    def movement(self, origin, dt):
        ''' PLayer Movement With Deplace Origin'''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            origin.x += self.speed * dt 
        if keys[pygame.K_RIGHT]:
            origin.x -= self.speed * dt 
        if keys[pygame.K_DOWN]:
            origin.y -= self.speed * dt 
        if keys[pygame.K_UP]:
            origin.y += self.speed * dt 

    def display(self, surface):
        ''' Display Player '''
        pygame.draw.rect(surface, 'gray', self.rect)
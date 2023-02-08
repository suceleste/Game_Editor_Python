# game.py
import pygame, sys
from pygame import Vector2 as vector
from pygame.mouse import get_pressed as mouse_pressed
from pygame.mouse import get_pos as mouse_pos
from settings import *
from player import Player

class Game:
    def __init__(self):
        ''' Viarable Game '''

        self.display_surface = pygame.display.get_surface()
        self.support_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.support_line_surf.set_alpha(150)

        self.origin = vector()
        self.offset = vector()
        self.pan_active = False
    
        self.player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    def event_loop(self):
        ''' Event Loop '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

            # Functions With Event
            #self.move_input(event)

    '''
    def move_input(self, event):
        # Move With The Mouse
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_pressed()[0]:
            self.pan_active = True
            self.offset = vector(mouse_pos()) - self.origin
        if not mouse_pressed()[0]:
            self.pan_active = False
        if self.pan_active :
            self.origin = vector(mouse_pos()) - self.offset
    '''

            
    def draw_tile_lines(self):
        cols = WINDOW_WIDTH // TILE_SIZE
        rows = WINDOW_HEIGHT // TILE_SIZE
        origin_offset = vector(
            x=self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE, 
            y=self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE
            )

        self.support_line_surf.fill("green")

        for col in range(cols + 1):
            x = origin_offset.x + col * TILE_SIZE
            pygame.draw.line(self.support_line_surf, LINE_COLOR, (x, 0), (x, WINDOW_HEIGHT))
        for row in range(rows + 1):
            y = origin_offset.y + row * TILE_SIZE
            pygame.draw.line(self.support_line_surf, LINE_COLOR, (0, y), (WINDOW_WIDTH, y))

        self.display_surface.blit(self.support_line_surf, (0,0))
    

    def run(self):
        ''' Main Function Run '''
        # World Settings and Display Origin=(0,0)World
        self.display_surface.fill('Gray')
        self.draw_tile_lines()
        pygame.draw.circle(self.display_surface, 'red', self.origin, 10)

        self.player.display(self.display_surface)
        self.player.movement(self.origin)
        self.event_loop()


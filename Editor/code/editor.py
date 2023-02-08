# editor.py
import pygame, sys
from pygame.mouse import get_pressed as mouse_pressed
from pygame.mouse import get_pos as mouse_pos
from pygame import Vector2 as vector
from settings import * 

class Editor:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		self.pan_active = False
		self.origin = vector(64,0)
		self.offset = vector()
		self.support_lines =pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.support_lines.set_colorkey('green')
		self.support_lines.set_alpha(30)


	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			self.pan_input(event)
	

	def pan_input(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and mouse_pressed()[1]:
			self.pan_active = True
			self.offset = vector(mouse_pos()) - self.origin
		if not mouse_pressed()[1]:
			self.pan_active = False
		
		if self.pan_active :
			self.origin = vector(mouse_pos()) - self.offset
	

	def draw_lines(self):
		cols = WINDOW_WIDTH // TILE_SIZE
		rows = WINDOW_HEIGHT // TILE_SIZE

		offset_origin = vector(
			x= self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
			y= self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE
		)

		self.support_lines.fill('green')

		for col in range(cols):
			x = offset_origin.x + col * TILE_SIZE
			pygame.draw.line(self.support_lines, LINE_COLOR, (x, 0), (x,WINDOW_HEIGHT))
		for row in range(rows):
			y= offset_origin.y + row * TILE_SIZE
			pygame.draw.line(self.support_lines, LINE_COLOR, (0,y), (WINDOW_WIDTH, y))

		self.display_surface.blit(self.support_lines, (0,0))


	def run(self):
		self.event_loop()
		self.draw_lines()
		pygame.draw.circle(self.display_surface, 'red', self.origin, 5)
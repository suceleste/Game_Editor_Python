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
		self.origin = vector()
		self.offset = vector()


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

	def run(self):
		self.event_loop()
		pygame.draw.circle(self.display_surface, 'red', self.origin, 5)
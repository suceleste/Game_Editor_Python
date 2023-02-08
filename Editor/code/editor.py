# editor.py
import pygame, sys
from settings import * 

class Editor:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()


	def event_loop(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

	def run(self):
		self.event_loop()
# main.py 
import pygame, sys
from settings import *
from editor import Editor
class Main:
	def __init__(self):
		pygame.init()

		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.Clock = pygame.time.Clock()

		self.editor = Editor()

	def run(self):
		while True :
			deltaTime = self.Clock.tick() // 1000

			self.display_surface.fill('gray')
			self.editor.run()
			pygame.display.update()

if __name__ == '__main__':
	main = Main()
	main.run()
# main.py
import pygame
from game import Game
from settings import *

# -- Main -- #
class Main:
	def  __init__(self):
		''' Variable Main '''
		pygame.init()

		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()

		self.game = Game()

	def run(self):
		''' Function Run :
				Launch The Game'''
		while True :

			deltaTime = self.clock.tick(FPS) / 1000

			self.game.run(deltaTime)
			pygame.display.update()

if __name__ == '__main__':
	main = Main()
	main.run()
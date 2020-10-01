'''a class to mange aliens'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""docstring for Alien"""
	def __init__(self, ai_settings,screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#create an alien an place it on the top left corner 
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#adding a space to the left of it that's equal to the alien's 
		#width and a spave above it 
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	def blitme(self):
		'''Draw the alien at the top left of the screen'''
		self.screen.blit(self.image,self.rect)


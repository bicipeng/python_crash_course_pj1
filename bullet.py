#when you use sprites, you can group related eles in your game 
#and act on all the grouped eles at once
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''a class to manage bullets fired form the ship'''

	def __init__(self,ai_settings,screen,ship):
		'''create a bullet object at the ship's current position.'''
		super(Bullet,self).__init__()
		self.screen = screen

		#create a bullet rect at (0,0) and then set correct position
		'''pygame.Rect(): requires the x,y coordinates fo the top-left corner of the rect
		and the width and height of the rect,initial at (0,0)'''
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

		#move the bullet to the correct location, since the bullet are shoot from the ship
		#its location should aligned with the ship's location
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#store the bullet's location as a decimal value
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		'''move the bullet up the screen'''
		#update the decimal point of the bullet
		self.y -= self.speed_factor
		#update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		'''draw the bullet on the screen.'''
		pygame.draw.rect(self.screen,self.color,self.rect)

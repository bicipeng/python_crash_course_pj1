import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		""" initialize the ship and set its startting position"""
		'''we defined ai_settins = Settings()  in the alien invatsion.py'''
		'''so you have all the attributes from settings included self.ship_speed_factor'''
		self.screen = screen
		self.ai_settings = ai_settings

		#load the ship image and get its rect.(pygame treates ele like retangles)
		#use get_rect() to access the surface's rect attribute
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#moving flag
		self.moving_right = False
		self.moving_left = False 

		#store a decimal value for the ship's center because rect can only store ints
		self.center = float(self.rect.centerx)

	def update(self):
		'''respond to keypresses and mouse events'''
		#update the ship's center value, not th erect.
		#rect is x,y axis 
		#self.rect.right(x-coordinate value of the right edge of the ship's rect)
		#if self.rect.right < self.screen_rect.right => ship hasn't reach the right edge of the screen
		#the same for the self.rect.left: the left boundary of the x-coordinate 
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		#update rect object form self.center
		#only the interger part of the self.center will be stored in self.rect.centerx
		self.rect.centerx = self.center


	def blitme(self):
		""" Draw the shp at its current location."""
		self.screen.blit(self.image,self.rect)
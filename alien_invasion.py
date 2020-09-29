#use sys to exit the game when player quits
#import from class : from file name import class
#import function from a file that only has one ft: import file_name
import pygame
import game_functions as gf 
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
	#initalize game and create a screen object
	pygame.init()
	ai_settings = Settings() #create an instance of the settings class
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#make a ship
	ship = Ship(ai_settings,screen)
	#make a group to store bullets in 
	bullets = Group()
	

	#start the main loop for the game
	while True:
		#pass the ship as an argument to checkenvets in gf
		#Watch for keyboard and mouse events using event.get()
		gf.check_events(ai_settings,screen,ship,bullets)

		#update the ship's position
		ship.update()
		bullets.update()

		#delete the bullet when it is off the screen s.t. it won't slow down game
		#make a copy of the group and work from the copy:we don't want to modify the 
		#group directly
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets))
		#Redraw the screen during each pass through the loop
		gf.update_screen(ai_settings,screen,ship,bullets)
		# pygame.display.flip() #new added

run_game()
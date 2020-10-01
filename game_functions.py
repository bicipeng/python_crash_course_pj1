#check_events 
#event is picked up by the pygame.event.get() method
#Each keypress is registered as a KEYDOWN event
#bullets is a group we create in ai.py bullets = Group


import sys
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	'''respond to key presses'''
	if event.key == pygame.K_RIGHT:
		#move the ship to the right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,ship):
	'''respond to key release'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	
def check_events(ai_settings,screen,ship,bullets):

	'''respond to keypresses and mouse events'''
	#pygame.event.get():stores events from users.i.e.quit,keyup,keydown
	#they all have attribute: type
	#in check_keydown_events ft, we pass in the keydown event as param
	#There are two types of key events in pygame: KEYDOWN and KEYUP. 
	#These events have an attribute key which is an integer representing a key on the keyboard.
	#that's why you cant access event.key
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_bullets(bullets):
	'''update the position of the bullets and get rid of old bullets'''
	#update bullet positions
	bullets.update() 
	#delete the bullet when it is off the screen s.t. it won't slow down game
	#make a copy of the group and work from the copy:we don't want to modify the 
	#group directly
	#get rid of the bullets that are disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
	'''fire a bullet if limit is not reached yet'''
		#check how many bullets exits before we create a new bullet
	if len(bullets) < ai_settings.bullets_allowed:
		#create a new bullet and add it to the bullets group
		new_bullet = Bullet(ai_settings,screen,ship)
		#using the add()method to store the new bullet in the group bullets
		bullets.add(new_bullet)
    

def update_screen(ai_settings,screen,ship,aliens,bullets):
	'''update images on the screen and flip to the new screen'''

	#Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	#redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	#make the most rectently drawn screen visible
	pygame.display.flip()

def create_alien(ai_settings,screen,aliens,alien_number):
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	#rect.x is the top left corner of the alien, 
	#each alien.x is going to be on the odd number spot: i.e. alien_width, 
	#3*alien_with,5*alien_with.... until reach the number of alien you want 
	alien.x = alien_width * (1 + 2 * alien_number) 
	alien.rect.x = alien.x
	aliens.add(alien)

def get_number_aliens_x(ai_settings,alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def create_fleet(ai_settings,screen,aliens):
	'''Create a full fleet of aliens'''
	#create an alien and find the number of aliens in a row
	#spacing between each alien is equal to one alien width
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)


	#create the first row of aliens
	for alien_number in range(number_aliens_x):
		#create an alien an place it in th erow
		create_alien(ai_settings,screen,aliens,alien_number)
	

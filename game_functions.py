#check_events 
#event is picked up by the pygame.event.get() method
#Each keypress is registered as a KEYDOWN event
#bullets is a group we create in ai.py bullets = Group


import sys
import pygame
from ship import Ship
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	'''respond to key presses'''
	if event.key == pygame.K_RIGHT:
		#move the ship to the right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		#create a new bullet and add it to the bullets group
		new_bullet = Bullet(ai_settings,screen,ship)
		#using the add()method to store the new bullet in the group bullets
		bullets.add(new_bullet)
    
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



def update_screen(ai_settings,screen,ship,bullets):
	'''update images on the screen and flip to the new screen'''

	#Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	#redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()


	#make the most rectently drawn screen visible
	pygame.display.flip()

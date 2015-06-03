# This will be are separate game for the battles.
import random, os.path
import renpy.display
import renpy.loader
import renpygame as pygame
from renpygame.locals import *

import renpy.store as store
import renpy.exports as renpy

import BattleGameEngine as BattleEngine

if not pygame.image.get_extended():
	raise SystemExit,"sorry, extended image module required"


# simple function to join two path strings
def os_path_join(a,b):
	return a + "/" + b

#game constants

def load_image(file):
	"loads an image, prepares it for game play"
	file = os_path_join('data',file)
	# Load file with 
	try:
		surface = renpy.display.pgrender.load_image(renpy.loader.load(file), file)
	except pygame.error:
		raise SystemExit,'Could not load image "%s" %s'%(file, pygame.get_error())
	return surface



def load_images(*files):
	imgs = []
	for file in files:
		imgs.append(load_image(file))
	return imgs	



class Player(pygame.sprite.Sprite):
	images = []
	speed = 2
	animationDelta = 150 # update animation every 150 ms
	distanceDelta = 6 # number of pixels to move to trigger a change animation.
	numberFrames = 4 # The number of frames
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[1]
		self.rect = self.image.get_rect(midbottom = SCREENRECT.midbottom)
		self.facing = -1
		self.distance = 0
		self.timeElapsed = 0
		self.ptr = 0


	def move(self,direction):
		if direction: self.facing = direction
		self.rect.move_ip(direction*self.speed,0)
		self.distance += direction * self.speed
		self.rect = self.rect.clamp(SCREENRECT)
	

	def updateTimeElapsed(self,TimeE):
		self.timeElapsed += TimeE


	def updateS(self,TimeE):
		#self.updateTimeElapsed(TimeE)
		self.timeElapsed += TimeE
		if self.timeElapsed >= self.animationDelta:
			self.timeElapsed = 0
			self.ptr += 1
			if self.ptr % 3 == 0:
				self.ptr = 0
			self.image = self.images[self.ptr]

	def updateD(self,changedDirection,direction):
		if(changedDirection):
			self.distance = 0
			if direction != 0:
				self.image = self.images[0]
			else:	
				self.image = self.images[1]
		else:
			if self.distance >= self.distanceDelta or self.distance <= -self.distanceDelta:
				self.distance = 0
				self.ptr += 1
				if self.ptr % 3 == 0:
					self.ptr = 0
				self.image = self.images[self.ptr]



















# size of screen
SCREENRECT     = Rect(0, 0, 640, 480)




class BattleEngine:

	@staticmethod
	def mainF():

    # Initialize pygame
	    pygame.init()


	     # Set the display mode
	    #f store._preferences.fullscreen:
	       # winstyle = FULLSCREEN
	   # else:
	    winstyle = 0

	    screen = renpy.display.pgrender.surface(SCREENRECT.size,True)
	    #bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	    #screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
	    #Player.images = load_images('fox_012.gif','fox_013.gif', 'fox_014.gif','fox_015.gif')
	    
	    

	    #decorate the game window
	    icon = pygame.transform.scale(Player.images[0], (32, 32))
	    #pygame.display.set_icon(icon)
	    #pygame.display.set_caption('Pygame Aliens')
	    pygame.mouse.set_visible(0)

	    # create the background
	    BGimage = load_image('BWF.jpg');
	    screen.blit(BGimage,(0,0))
	    #pygame.display.flip()
	

	    all = pygame.sprite.RenderUpdates()
	    Player.containers = all


	    clock = pygame.time.Clock()
	    player = Player()



	    
	    prev_direction = 0
	    # here all is all the sprites.
	    changedDirection = False
	    animationTime = .1
	    while True:
	    

	    	updateAnimation = False
	    	#resetAnimation = True
	    	changedDirection = False
	    	




	    

	    	for event in pygame.event.get():
	    		if event.type == QUIT or \
	    		(event.type == KEYDOWN and event.key == K_ESCAPE):
	    			return score
	    		
	    			
	    			

			keystate = pygame.key.get_pressed()


		
	    


			all.clear(screen,BGimage)

			#player.updateS(clock.tick(40))

			

			direction = keystate[K_RIGHT] - keystate[K_LEFT]

			if direction != prev_direction: changedDirection = True


			player.updateD(changedDirection,direction)

	        # we need to know when to start the animation walking loop this will be when the previous direction is not the same as current direction. 
	    	#if prev_direction != direction:
	    	#	changedDirection = True
	    	
	    
	        # if the direction changed update
	        		
	        #player.updateD(changedDirection)
	        #if changedDirection == True:

	           
			
			player.move(direction)
			

			prev_direction = direction
			#dirty = all.draw(screen)
			all.draw(screen)
			#pygame.display.update()


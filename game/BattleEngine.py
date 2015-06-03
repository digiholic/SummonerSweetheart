# This will be are separate game for the battles.
import renpy.display

class BattleEngine:


	def mainF():
    # Initialize pygame
	    pygame.init()


	     # Set the display mode
	    #f store._preferences.fullscreen:
	       # winstyle = FULLSCREEN
	   # else:
	    winstyle = 0


	    #bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	    #screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
	    #Player.images = load_images('fox_012.gif','fox_013.gif', 'fox_014.gif','fox_015.gif')
	    
	    BGimage = load_image('BWF.jpg');

	    #decorate the game window
	    icon = pygame.transform.scale(Player.images[0], (32, 32))
	    #pygame.display.set_icon(icon)
	    #pygame.display.set_caption('Pygame Aliens')
	    #pygame.mouse.set_visible(0)

	    # create the background
	    bgdtile = load_image('background.gif')
	    background = renpy.display.pgrender.surface(SCREENRECT.size,True)
	    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
	    	background.blit(bgdtile,(x,0))
	    screen.blit(background,(0,0))
	    pygame.display.flip()

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


			if keystate[K_q]:
	    			#player.kill()
	    			
	    			screen.blit(BGimage,(0,0))
	    			all.clear(screen,BGimage)
	    			pygame.display.flip()
	    			pygame.display.update()
	    			

	    	else:
	    


				all.clear(screen,background)

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
				pygame.display.update()


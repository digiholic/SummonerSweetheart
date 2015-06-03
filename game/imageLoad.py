
import random, os.path

import renpygame as pygame

from renpygame.locals import *

import renpy.store as store
import renpy.exports as renpy
import renpy.display

import BattleGameEngine as BattleEngine

if not pygame.image.get_extended():
	raise SystemExit,"sorry, extended image module required"

# simple function to join two path strings
def os_path_join(a,b):
	if a == []:
		return b
	else:  
		return a + "/" + b





def load_image(fp,file,alpha = False):
	"loads an image, prepares it for game play"
	file = os_path_join(fp,file)
	# Load file with 
	try:
		surface = renpy.display.pgrender.load_image(renpy.loader.load(file), file)
	except pygame.error:
		raise SystemExit,'Could not load image "%s" %s'%(file, pygame.get_error())
	return surface



def load_images(*files):
	imgs = []
	for file in files:
		imgs.append(load_image('data',file,True))
	return imgs	


def blit_alpha(target, source, location, area, opacity):
		x = location[0]
		y = location[1]
		temp = renpy.display.pgrender.surface((source.get_width(), source.get_height()),True)
		temp.blit(target, (-x, -y))
		temp.blit(source, (0, 0))
		temp.set_alpha(opacity)        
		target.blit(temp, location,area)

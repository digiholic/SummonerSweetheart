# Building the scene. 

# initialize all background tile images
# initalize all minions
# initialize all animated background images



import random, os.path

import renpygame as pygame

from renpygame.locals import *

import renpy.store as store
import renpy.exports as renpy

import BattleGameEngine as BattleEngine

if not pygame.image.get_extended():
    raise SystemExit,"sorry, extended image module required"


# Builds the scene and initalizes all assets
class GameState:


	def __init__(self,scene_dict):
		self.


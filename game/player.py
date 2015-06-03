import random, os.path

import renpygame as pygame

from renpygame.locals import *

import renpy.store as store
import renpy.exports as renpy

import BattleGameEngine as BattleEngine
from champion import *

import screenObjects

if not pygame.image.get_extended():
	raise SystemExit,"sorry, extended image module required"

SCREENRECT     = Rect(0, 0, 1024, 768)


#import gameConstants


class Player(pygame.sprite.Sprite):
	speed = 1
	animationDelta = 500 # update animation every 150 ms
	distanceDelta =6 # number of pixels to move to trigger a change animation.
	numberFrames = 6 # The number of frames

	idleImages = []
	walkImages = []



	
	def __init__(self,org):
		pygame.sprite.Sprite.__init__(self, self.containers)
		#super(Player,self).__init__(self, self.containers)
		self.pos = org[0]  	# The initial pixel of the character.
		self.images = self.walkImages
		self.image = self.images[0]
		self.rect = self.image.get_rect(center = org)
		self.width = self.image.get_width()
		self.facing = -1
		self.distance = 0
		self.timeElapsed = 0
		self.direction = 0
		self.ptrW = 0
		self.ptrI = 0
		self.animationDelta = 150




	def move(self,direction,changedDirection):
		if direction == 0:
			self.images = self.idleImages
			self.ptrI = 0
		else:
			self.images = self.walkImages
			self.direction = direction
			if direction: self.facing = direction
			#self.rect.move_ip(direction*self.speed,0)
			self.distance += direction * self.speed
			self.pos += direction * self.speed
			self.rect = self.rect.clamp(SCREENRECT)
		

	def updateTimeElapsed(self,TimeE):
		self.timeElapsed += TimeE


	def updateS(self,TimeE):
		#self.updateTimeElapsed(TimeE)
		self.timeElapsed += TimeE
		if self.timeElapsed >= self.animationDelta:
			self.timeElapsed = 0
			self.ptrI += 1
			if self.ptrI % len(self.idleImages) == 0:
				self.ptrI = 0
			self.image = self.images[self.ptrI]
			self.image.set_colorkey((0,0,0))

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
				self.ptrW += 1
				if self.ptrW % 6 == 0:
					self.ptrW = 0
				self.image = self.images[self.ptrW]

		self.image.set_colorkey((0,0,0))







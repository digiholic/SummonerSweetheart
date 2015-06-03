import renpygame as pygame
from imageLoad import *

#import gameConstants
SCREENRECT     = pygame.Rect(0, 0, 1024, 768)



# rough code for setting transition objects
def buildTransitionTile(images,numLoops,posX):
	# images are a list of image objects of form : [left,midlle,right]
	hOffset = 100
	

	Ltile = TileImage(images[0],(SCREENRECT[2]-1,SCREENRECT[3] - images[0].get_height() - hOffset),1,posX)
	Mtile = TileImage(images[1],(SCREENRECT[2]-1,SCREENRECT[3] - images[0].get_height()- hOffset),numLoops,images[0].get_width()+posX)
	Rtile = TileImage(images[2],(SCREENRECT[2]-1,SCREENRECT[3] - images[0].get_height()- hOffset),1,posX  + (numLoops +1) * images[0].get_width())


	return Ltile,Mtile,Rtile


class TileImage(pygame.sprite.Sprite):
	#pygame.init()

	blankImage = []
	backgroundImage = []
	#backgroundImage.fill(pygame.color.Color(181,238,255))
	#alphaStatic = load_image()

	def __init__(self,img,org,NumLoops,PosX = 0):
		self.isFirst = False
		self.image = img
		#self.image.set_colorkey((255,255,255))
		#self.imgPath = img
		#self.image = load_image('data',self.imgPath,True)
		self.offSet = 0
		#self.origin = (SCREENRECT[2]-1,SCREENRECT[3]-(self.image.get_width()))
		self.origin = org
		self.active = False
		self.numLoops = NumLoops
		self.posX = PosX
		self.dx = 1 # direction to scroll in background (left)
		self.timesLooped = 0
		self.finished = False
		self.changedDirection = False




	def updateE(self,Background,Player):
		self.changedDirection = False
		if self.dx != Player.direction:
			self.changedDirection = True
		self.dx = Player.direction
		self.isActive(Player.pos)

		if self.active == True:
			self.updateOS()
			self.blipOffset(Background)


	def updateOS(self):
		self.offSet += self.dx
		if self.offSet % self.image.get_width() == 0 and self.dx == 1: 
			self.timesLooped += 1
			self.offSet = 0

			if self.numLoops == -1:
				pass
			elif self.timesLooped >= self.numLoops:
				self.active = False
				self.finished = True
		elif self.offSet == 0 and self.dx == -1:
			self.offSet = self.image.get_width()
			# if self.timesLooped >= self.numLoops:
			# 	self.active = False
			# 	self.finished = True





	# def blipOffset(self,background):
	# # srcImage: The source surface, the tile or background image
	# # background: the actual background as rendered


	# 	#self.image = load_image('data',self.imgPath,True)

	# 	#SCREENRECT     = Rect(0, 0, 1024, 768)

	# #	blankImage = pygame.Surface((1,768))
	# 	#blankImage.fill(pygame.color.Color(181,238,255))


	# 	srcImgW = self.image.get_width()
	# 	srcImgH = self.image.get_height()

		
	# 	# the areaNewImage acts as a constant which is simply srcImgH.

	# 	# image offset acts as a scanning variable across the image in x direction.
	# 	#srcArea = pygame.Rect((0,0),(1,srcImgH)
	# 	srcArea = pygame.Rect((self.offSet,0),(1,srcImgH))
	# 	#imageBlank = load_image('data','redPit/redpit_alpha.png')

	# 	#imageBlank.blit(self.image,self.origin,srcArea)
	# #				background.blit(bgdtile,origin2,source_area2)
	# 	#imageBlank.blit(self.image,self.origin,srcArea)
	# 	#background = pygame.Surface(SCREENRECT.size)
	# 	if self.isFirst == True:
	# 		self.blankImage.blit(self.image,(0,0),srcArea)
	# 		background.blit(self.blankImage,self.origin) 
	# 	else:
	# 		background.blit(self.image,self.origin,srcArea)   


	def blipOffset(self,background):
	# srcImage: The source surface, the tile or background image
	# background: the actual background as rendered


		#self.image = load_image('data',self.imgPath,True)

		#SCREENRECT     = Rect(0, 0, 1024, 768)

	#	blankImage = pygame.Surface((1,768))
		#blankImage.fill(pygame.color.Color(181,238,255))


		srcImgW = self.image.get_width()
		srcImgH = self.image.get_height()

		
		# the areaNewImage acts as a constant which is simply srcImgH.

		# image offset acts as a scanning variable across the image in x direction.
		#srcArea = pygame.Rect((0,0),(1,srcImgH)

		if self.changedDirection == True:
		
			# going forward
			if self.dx == 1:
				pass
				# diff = float(SCREENRECT[2] + self.offSet)
				# if diff > srcImgW:
				# 	self.offSet = srcImgW * ((diff) % srcImgW)/srcImgW
				
			# going backward
			elif self.dx == -1:
				diff = float(SCREENRECT[2] - self.offSet)
				if diff < 0:
					self.offSet -= SCREENRECT[2]
				else:
					self.offSet = srcImgW * (1 - ((diff) % srcImgW)/srcImgW)
					self.offSet = round(self.offSet)

		if self.dx == 1:

			srcArea = pygame.Rect((self.offSet,0),(1,srcImgH))
		#imageBlank = load_image('data','redPit/redpit_alpha.png')
		elif self.dx == -1:

			srcArea = pygame.Rect((self.offSet,0),(1,srcImgH))
		#imageBlank.blit(self.image,self.origin,srcArea)
	#				background.blit(bgdtile,origin2,source_area2)
		#imageBlank.blit(self.image,self.origin,srcArea)
		#background = pygame.Surface(SCREENRECT.size)


		if self.isFirst == True:
			self.blankImage.blit(self.image,(0,0),srcArea)
			background.blit(self.blankImage,self.origin) 
		else:
			if self.dx == 1:
				background.blit(self.image,self.origin,srcArea)
			elif self.dx == -1: 
				background.blit(self.image,(0,0),srcArea)

	def isActive(self,playerPos):
		if playerPos >= self.posX and self.finished == False:
			self.active = True




